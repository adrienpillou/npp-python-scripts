line_count = editor.getLineCount()
editor.beginUndoAction()
for i in range(line_count):
    value = editor.getLine(i).strip()
    editor.replaceWholeLine(i, value.zfill(10) + "\r")
editor.documentEnd()
editor.deleteBack()
editor.endUndoAction()