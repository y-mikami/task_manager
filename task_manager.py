import json
import os

TASKS_FILE = "tasks.json"


def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_tasks(tasks):
    with open(TASKS_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)


def add_task(title):
    tasks = load_tasks()
    task = {"id": len(tasks) + 1, "title": title, "done": False}
    tasks.append(task)
    save_tasks(tasks)
    print(f"タスクを追加しました: {title}")


def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("タスクはありません。")
        return
    print("\n--- タスク一覧 ---")
    for task in tasks:
        status = "✓" if task["done"] else "○"
        print(f"[{task['id']}] {status} {task['title']}")
    print()


def complete_task(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
            save_tasks(tasks)
            print(f"タスクを完了にしました: {task['title']}")
            return
    print(f"ID {task_id} のタスクが見つかりません。")


def delete_task(task_id):
    tasks = load_tasks()
    new_tasks = [t for t in tasks if t["id"] != task_id]
    if len(new_tasks) == len(tasks):
        print(f"ID {task_id} のタスクが見つかりません。")
        return
    save_tasks(new_tasks)
    print(f"ID {task_id} のタスクを削除しました。")


def show_help():
    print("""
使い方:
  python task_manager.py add <タスク名>    タスクを追加
  python task_manager.py list             タスク一覧を表示
  python task_manager.py done <ID>        タスクを完了にする
  python task_manager.py delete <ID>      タスクを削除する
""")


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        show_help()
        sys.exit(0)

    command = sys.argv[1]

    if command == "add":
        if len(sys.argv) < 3:
            print("タスク名を入力してください。例: python task_manager.py add 買い物")
        else:
            add_task(" ".join(sys.argv[2:]))

    elif command == "list":
        list_tasks()

    elif command == "done":
        if len(sys.argv) < 3:
            print("IDを入力してください。例: python task_manager.py done 1")
        else:
            complete_task(int(sys.argv[2]))

    elif command == "delete":
        if len(sys.argv) < 3:
            print("IDを入力してください。例: python task_manager.py delete 1")
        else:
            delete_task(int(sys.argv[2]))

    else:
        print(f"不明なコマンド: {command}")
        show_help()
