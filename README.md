# Task Manager（タスク管理ツール）

ターミナルで気軽に使うシンプルなタスク管理ツールです。タスクの追加・一覧表示・完了・削除ができます。

## 必要な環境

- Python 3

## 使い方

```bash
# タスクを追加
python task_manager.py add <タスク名>

# タスク一覧を表示
python task_manager.py list

# タスクを完了にする（ID を指定）
python task_manager.py done <ID>

# タスクを削除する（ID を指定）
python task_manager.py delete <ID>
```

## 例

```bash
python task_manager.py add 買い物
python task_manager.py add メール返信
python task_manager.py list
python task_manager.py done 1
python task_manager.py delete 2
```

## データ

タスクは同じフォルダ内の `tasks.json` に保存されます。

## 更新履歴

- 2025/03 初版（ローカルで編集）
- 2025/03 初版（GitHubで編集）
- 2025/03 共同編集の練習
- 2025/03 ローカルで追記

## ブランチ練習で追加

- この行は `add-readme-section` ブランチで追加しました。