import praw
import configparser


config = configparser.ConfigParser()
config.read('conf.ini')
reddit_user = config['REDDIT']['reddit_user']
reddit_pass = config['REDDIT']['reddit_pass']
reddit_client_id = config['REDDIT']['reddit_client_id']
reddit_client_secret = config['REDDIT']['reddit_client_secret']
reddit_target_subreddits = [i.strip() for i in config['REDDIT']['reddit_target_subreddits'].split(',')]

reddit = praw.Reddit(
    username=reddit_user,
    password=reddit_pass,
    client_id=reddit_client_id,
    client_secret=reddit_client_secret,
    user_agent='Reddit Automod Config Sync (by u/impshum)'
)

with open('automod.yaml') as f:
    automod_text = f.read()


def edit_automod(subreddit, automod_text):
    sub = reddit.subreddit(subreddit)
    sub.wiki['config/automoderator'].edit(automod_text)
    print(f'Updated automod config on r/{subreddit}')


def main():
    for subreddit in reddit_target_subreddits:
        edit_automod(subreddit, automod_text)


if __name__ == '__main__':
    main()
