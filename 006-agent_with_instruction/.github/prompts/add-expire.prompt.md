---
mode: agent
tools: ['changes', 'codebase', 'editFiles', 'extensions', 'fetch', 'findTestFiles', 'githubRepo', 'new', 'openSimpleBrowser', 'problems', 'readCellOutput', 'runCommands', 'runNotebooks', 'runTasks', 'runTests', 'search', 'searchResults', 'terminalLastCommand', 'terminalSelection', 'testFailure', 'usages', 'vscodeAPI', 'playwright']
---

entityの Task に、有効期限の日付の属性を追加して、APIとフロントエンドの両方で対応して。
Task は以下のファイルに定義されているよ。

API: todo_api/domain/entity/entity.py
フロントエンド: todo_frontend/src/entity/task.ts

todo_frontend/src/views/taskList.tsx でタスクの有効期限を表示し、
新規タである todo_frontend/src/views/newTask.tsx で、有効期限を入力できるようにして。
入力期限は、カレンダー入力ができるイブラリ react-datepicker を導入して利用して。
