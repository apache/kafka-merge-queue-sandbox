import asfquart

from quart import request, jsonify
from yaml import load
from yaml import Loader

app = asfquart.construct("merge-queue-webhook")

with open("config.yml") as fp:
    config = load(fp, Loader=Loader)

gh_user_map = config.get("gh-user-map", {})


@app.route('/webhook', methods=['POST'])
async def webhook_receiver():
    payload = await request.get_json()
    event = request.headers.get("X-Github-Event")
    action = payload.get("action")

    if event == "pull_request" and action == "enqueued":
        pr_number = payload.get("number")
        login = payload.get("sender").get("login")
        asf_id = gh_user_map.get(login)
        pull_request = payload.get("pull_request")
        title = pull_request.get("title")
        print(f"User {login} (Apache ID {asf_id}) added PR #{pr_number} ({title}) to merge queue.")
    elif event == "pull_request" and action == "dequeued":
        pr_number = payload.get("number")
        reason = payload.get("reason")
        pull_request = payload.get("pull_request")
        if reason.lower() == "merge":
            merge_commit_sha = pull_request.get("merge_commit_sha")
            title = pull_request.get("title")
            login = payload.get("sender").get("login")
            asf_id = gh_user_map.get(login)
            print(f"User {login} (Apache ID {asf_id}) merged PR #{pr_number} ({title}). Merge SHA is {merge_commit_sha}")
    elif event == "merge_group" and action == "checks_requested":
        print("Merge group!!")
        merge_group = payload.get("merge_group", {})
        login = payload.get("sender").get("login")
        asf_id = gh_user_map.get(login)
        base = merge_group.get("base_sha")
        head = merge_group.get("head_sha")
        print(f"User {login} (Apache ID {asf_id}) merged commits after {base} up until {head} via merge queue")
    else:
        print(f"Received webhook event {event} with action {action}")

    return jsonify({'message': 'Webhook received successfully'}), 200
        

if __name__ == '__main__':
    asfquart.APP.run(port=3000)
