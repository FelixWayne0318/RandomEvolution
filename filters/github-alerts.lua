-- Translate GitHub-flavored alert blockquotes into Quarto callouts.
--
-- Source (GitHub-rendered as alert, Quarto would render as plain blockquote):
--     > [!NOTE]
--     > **Optional bold title**
--     >
--     > body...
--
-- Output (Quarto-rendered as callout):
--     ::: {.callout-note title="Optional bold title"}
--     body...
--     :::

local alert_map = {
  NOTE      = "note",
  TIP       = "tip",
  IMPORTANT = "important",
  WARNING   = "warning",
  CAUTION   = "caution",
}

local function strip_leading_whitespace(inlines)
  while #inlines > 0 do
    local t = inlines[1].t
    if t == "SoftBreak" or t == "LineBreak" or t == "Space" then
      table.remove(inlines, 1)
    else
      break
    end
  end
end

local function extract_title(blocks)
  -- If first remaining block is a Para or Header containing only a Strong,
  -- treat that as the callout title.
  if #blocks == 0 then return nil end
  local b = blocks[1]
  if b.t == "Header" then
    local title = pandoc.utils.stringify(b.content)
    table.remove(blocks, 1)
    return title
  end
  if b.t == "Para" and #b.content == 1 and b.content[1].t == "Strong" then
    local title = pandoc.utils.stringify(b.content[1])
    table.remove(blocks, 1)
    return title
  end
  return nil
end

function BlockQuote(elem)
  local blocks = elem.content
  if #blocks == 0 then return nil end

  local first = blocks[1]
  if first.t ~= "Para" or #first.content == 0 then return nil end

  local first_inline = first.content[1]
  if first_inline.t ~= "Str" then return nil end

  local alert_type = first_inline.text:match("^%[!(%w+)%]$")
  if not alert_type then return nil end

  local callout_type = alert_map[alert_type:upper()]
  if not callout_type then return nil end

  -- Drop the [!XXX] marker and any whitespace right after it.
  table.remove(first.content, 1)
  strip_leading_whitespace(first.content)

  -- If the marker was on its own line, the first paragraph is now empty.
  if #first.content == 0 then
    table.remove(blocks, 1)
  end

  local title = extract_title(blocks)

  local attr_kv = {}
  if title then attr_kv.title = title end

  return pandoc.Div(
    blocks,
    pandoc.Attr("", { "callout-" .. callout_type }, attr_kv)
  )
end
