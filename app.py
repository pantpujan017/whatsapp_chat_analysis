import streamlit as st 
import preprocessor,helper
import matplotlib.pyplot as plt

st.sidebar.title('Whatsapp Chat Analyzer')

uploaded_file=st.sidebar.file_uploader("Choose a file")
if uploaded_file is not None:
    bytes_data=uploaded_file.getvalue()
    data=bytes_data.decode('utf-8')
    df=preprocessor.preprocess(data)

    


    user_list=df['user'].unique().tolist()
    if 'group_notification' in user_list:
        user_list.remove('group_notification')
    user_list.sort()
    user_list.insert(0,"Overall")
    selected_user=st.sidebar.selectbox("Show analysis wrt",user_list)

    if st.sidebar.button("Show analysis"):

        num_messages,words,num_media_messages,num_links=helper.fetch_stats(selected_user,df)
        st.title('Top Statistics')

        col1,col2,col3,col4=st.columns(4)

        

        with col1:
            st.header("Total messages")
            st.title(num_messages)
        with col2:
            st.header("Total words")
            st.title(words)
        with col3:
            st.header("Total medias shared")
            st.title(num_media_messages)
        with col4:
            st.header("Total links shared")
            st.title(num_links)

        
        st.title('Monthly Timeline')
        timeline=helper.monthly_timeline(selected_user,df)
        fig,ax=plt.subplots()
        ax.plot(timeline['time'],timeline['message'])
        plt.xticks(rotation='vertical')
        st.pyplot(fig)

        st.title('Daily Timeline')
        daily_timeline=helper.daily_timeline(selected_user,df)
        fig,ax=plt.subplots()
        ax.plot(daily_timeline['only_date'],daily_timeline['message'])
        plt.xticks(rotation='vertical')
        st.pyplot(fig)



        st.title('Acitvity Map')
        col1,col2=st.columns(2)

        with col1:
            st.header('Most busy day')
            busy_day=helper.weekly_activity_map(selected_user,df)
            fig,ax=plt.subplots()
            ax.bar(busy_day.index,busy_day.values)
            st.pyplot(fig)

        if selected_user == 'Overall':
            st.title('Most busy user')
            x,new_df=helper.most_busy_users(df)
            fig,ax=plt.subplots()
            
            col1,col2=st.columns(2)

            with col1:
                ax.bar(x.index,x.values)
                st.pyplot(fig)
            with col2:
                st.dataframe(new_df)
        
        st.title("Word Cloud")
        df_wc=helper.create_wordcloud(selected_user,df)
        fig,ax=plt.subplots()
        ax.imshow(df_wc)
        st.pyplot(fig)

        most_common_df=helper.most_common_words(selected_user,df)


        fig,ax=plt.subplots()
        ax.barh(most_common_df[0],most_common_df[1])
        plt.xticks(rotation='vertical')
        st.title('Most common words')
        st.pyplot(fig)


        emoji_df=helper.emoji_helper(selected_user,df)
        st.title('Emoji Analysis')

        col1,col2=st.columns(2)


        with col1:
            st.dataframe(emoji_df)

        with col2:
            fig,ax=plt.subplots()
            ax.pie(emoji_df['count'], labels=emoji_df['emoji'], autopct='%1.1f%%')
            st.pyplot(fig)





