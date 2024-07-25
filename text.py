import streamlit as st
from utills import text,embeddings
from streamlit_chat import message
import pandas as pd



def main():


    st.set_page_config(page_title='converse com seus arquivos', page_icon=':books')
    user_question = st.text_input("faça uma pergunta?")
   
    if 'conversation' not in st.session_state:
        st.session_state.conversation = None

    if user_question:
        response = st.session_state.conversation(user_question)['chat_history']
        for i, text_message in enumerate(response):
            if i % 2 == 0:
                message(text_message.content, is_user=True, key=str(i) + '_user')
            else:
                message(text_message.content, is_user=False, key=str(i) + '_bot')

    

    
    
    with st.sidebar:
        st.subheader('seus arq')
        uploaded_file = st.file_uploader("Faça o upload de um arquivo CSV", type='csv')
        if uploaded_file is not None:
            data = pd.read_csv(uploaded_file)
            st.write(data)



        #df = pd.read_csv("./transcript_table(1).csv")
        
        #leitor_csv = st.file_uploader("faça o carregamento de seus pdf")
    #def convert_df(df):
        #return df.to_csv(index = False).encode('utf-8')
    #csv = convert_df(df)

    #st.download_button(
        #"press to Download",
        #csv, "file.csv")
    chunks=.create_chunks()

    vectorstore = embeddings.create_vectorstores(chunks)
    st.session_state.conversation = embeddings.create_conversation_chain(vectorstore)

if __name__ == '__main__':
    main()
 
