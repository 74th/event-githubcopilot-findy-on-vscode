# Agent機能

## GitHub MCP Server

- VS CodeのWebサイトから、MCPのページを開き、GitHubのMCP Serverをインストールする
- MCP Serverを、サイドバーの拡張機能から起動する
- 以下のようにAgentモードで依頼する

```
https://github.com/74th/event-githubcopilot-findy というリポジトリに、「GitHub CopilotのAgentモードのテストコードを追加する」というIssueを作ってもらえる？
```

## Playwright MCPの活用

- TODOアプリを作ってあり、以下のコマンドで起動する

```
# APIサーバ(Python)の起動
uv run python -m todo_api.server.api

# フロントエンドサーバ(React)の起動
cd todo_frontend && npm start
```

- TODOアプリの軽い紹介をする
- VS CodeのWebサイトから、MCPのページを開き、PlaywrightのMCP Serverをインストールする
- MCP Serverを、サイドバーの拡張機能から起動する
- Playwright MCPを使って、以下のようなテストを行う

```
MCP ToolのPlaywrightを使って、http://localhost:3000にアクセスし、以下の手順を行って。
なお、サーバは起動済みだよ。

1. Task Title の入力欄に「新しいタスクのテスト」と入力する
2. 「Add」ボタンをクリックする
3. タスクの一覧として、「新しいタスクのテスト」が表示されることを確認する
```
