from operator import itemgetter
from plotly.graph_objs import Bar
from plotly import offline

import requests

# Make an API call and store the response.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Process information about each submission.
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:30]:
    # Make a seperate API call for each submission.
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()
    
    # Build a dictionary for each article.
    try: 
        submission_dict = { 
            'title': response_dict['title'],
            'hn_link': f"https://news.ycombinator.com/item?id={submission_id}",
            'comments': response_dict['descendants'],
        }
    except KeyError:
                submission_dict = {
            'title': response_dict['title'],
            'hn_link': f"https://news.ycombinator.com/item?id={submission_id}",
            'comments': 0,
        }
    submission_dicts.append(submission_dict)
    
submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),
                          reverse=True)

article_links, comments, lables, shortened_titles = [], [], [], []
for submission_dict in submission_dicts:
    title = submission_dict['title']
    url = submission_dict['hn_link']
    article_link = f"<a href={url}>{title}</a>"
    article_links.append(article_link)
    
    shortened_titles.append(title[0:40])
    
    comments.append(submission_dict['comments'])
    
    
    
    
# Make visualization
data = [{
    'type': 'bar',
    'x': shortened_titles,
    'y': comments,
    'hovertext': article_links,
    'marker': {
        'color': 'rgb(60, 100, 150)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
    },
    'opacity': 0.6,
}]

my_layout = {
    'title': 'Most Commented on Articles on Hacker News',
    'titlefont': {'size': 28},
    'xaxis': {
        'title': 'Article Names',
        'titlefont': {'size': 18},
        'tickfont': {'size': 12},
        },
    'yaxis': {
        'title': 'Number of Comments',
        'titlefont': {'size': 18},
        'tickfont': {'size': 12},
        },
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='popular_hn_articles.html')