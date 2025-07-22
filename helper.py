from urlextract import URLExtract
from wordcloud import WordCloud
import pandas as pd 
from collections import Counter
import emoji


extract=URLExtract()




def fetch_stats(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    num_messages = df.shape[0]
    words = []
    for message in df['message']:
        words.extend(message.split())

    
    num_media_messages=df[df['message'].str.contains(r'<attached:',na=False)].shape[0]

    links=[]
    for message in df['message']:
        links.extend(extract.find_urls(message))

    return num_messages, len(words),num_media_messages,len(links)


def most_busy_users(df):
    x = df['user'].value_counts()
    df = round((x / x.sum()) * 100, 2).reset_index()
    df.columns = ['name', 'percent']
    return x.head(), df


def create_wordcloud(selected_user,df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    wc=WordCloud(width=500,height=500,min_font_size=10,background_color='white')
    df_wc=wc.generate(df['message'].str.cat(sep=" "))
    return df_wc

def most_common_words(selected_user,df):
    f=open('nenglish_stopwords.txt','r')
    stop_words=f.read()

    if selected_user!='Overall':
        df=df[df['user']==selected_user]
    temp=df[df['user']!='group_notification']
    temp = temp[~temp['message'].str.contains(r'<attached:', na=False)]


    words=[]

    for message in temp['message']:
        for word in message.lower().split():
            if word not in stop_words:
                words.append(word)

    most_common_df = pd.DataFrame(Counter(words).most_common(20))
    return most_common_df

def emoji_helper(selected_user,df):
    if selected_user!='Overall':
        df=df[df['user']==selected_user]
    
    emojis=[]
    for message in df['message']:
        if isinstance(message,str):
            emojis.extend([c for c in message if c in emoji.EMOJI_DATA])
    emoji_df=pd.DataFrame(Counter(emojis).most_common(),columns=['emoji','count'])
    return emoji_df


def monthly_timeline(selected_user,df):

    if selected_user!='Overall':
        df=df[df['user']==selected_user]

    timeline=df.groupby(['year','month_num','month']).count()['message'].reset_index()

    time=[]
    for i in range(timeline.shape[0]):
        time.append(timeline['month'][i]+"-"+str(timeline['year'][i]))

    timeline['time']=time
    return timeline


def daily_timeline(selected_user,df):
    if selected_user!='Overall':
        df=df[df['user']==selected_user]
    
    daily_timeline=df.groupby('only_date').count()['message'].reset_index()

    return daily_timeline

def weekly_activity_map(selected_user,df):
    if selected_user!='Overall':
        df=df[df['user']==selected_user]

    return df['day_name'].value_counts()







