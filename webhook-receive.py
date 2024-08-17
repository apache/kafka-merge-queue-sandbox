from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook_receiver():
    data = request.json
    event = data.get("event")
    payload = data.get("payload")
    action = payload.get("action")

    if event == "pull_request" and action == "enqueued":
        pr_number = payload.get("number")
        login = payload.get("sender").get("login")
        pull_request = payload.get("pull_request")
        title = pull_request.get("title")
        print(f"User {login} added PR #{pr_number} ({title}) to merge queue.") 
    elif event == "pull_request" and action == "dequeued":
        pr_number = payload.get("number")
        reason = payload.get("reason")
        pull_request = payload.get("pull_request")
        if reason.lower() == "merge":
            merge_commit_sha = pull_request.get("merge_commit_sha")
            title = pull_request.get("title")
            login = payload.get("sender").get("login")
            print(f"User {login} merged PR #{pr_number} ({title}). Merge SHA is {merge_commit_sha}") 
    elif event == "merge_group" and action == "checks_requested":
        print("Merge group!!")
        merge_group = payload.get("merge_group", {})
        login = payload.get("sender").get("login")
        base = merge_group.get("base_sha")
        head = merge_group.get("head_sha")
        print(f"User {login} merged commits after {base} up until {head} via merge queue")
    else:
        print(f"Received webhook event {event} with action {actio}: {payload}")

    return jsonify({'message': 'Webhook received successfully'}), 200
        

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=3000)
