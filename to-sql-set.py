editor.beginUndoAction()
editor.rereplace(r"^", r"'")
editor.rereplace(r"$", r"',")
line_count = editor.getLineCount()
editor.gotoLine(line_count)
editor.deleteBack()
editor.newLine()
editor.addText(")")
editor.documentStart()
editor.addText("(")
editor.newLine()
editor.endUndoAction()
