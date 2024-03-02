import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

bike_share = pd.read_csv('bike_share.csv')

st.sidebar.title('Navigation')
selected_section = st.sidebar.selectbox('Select a section', ['Home', 'Section 1', 'Section 2'])

if selected_section == 'Home':
    st.title('Welcome!')
    st.title('Bike Sharing Dashboard')
    st.write('Dashboard sederhana untuk menampilkan data Pengaruh musim dan perbedaan hari dalam jumlah sewa sepeda')

elif selected_section == 'Section 1':
    st.title('Analysis 1')
    fig, ax = plt.subplots()
    seasonal_data = bike_share.groupby('season_daily')['cnt_daily'].mean()
    season_names = ['Spring', 'Summer', 'Fall', 'Winter']
    ax.bar(season_names, seasonal_data)
    ax.set_ylabel('Rata-rata jumlah sewa sepeda per hari')
    ax.set_title('Pengaruh musim terhadap jumlah Sewa Sepeda per hari')
    st.pyplot(fig)
    with st.expander('See explanation'):
        st.write('Jumlah sepeda yang disewa bergantung terhadap musim. Dari hasil diatas dapat disimpulkan bahwa Jumlah sepeda yang disewa lebih banyak jumlahnya pada saat musim Fall/ Gugur')


elif selected_section == 'Section 2':
    st.title('Analysis 2')
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.boxplot(x="workingday_daily", y="cnt_daily", data=bike_share, ax=ax)
    ax.set_title("Perbedaan antara Working Day dan Holiday dalam jumlah sewa sepeda")
    ax.set_xlabel("Working day")
    ax.set_ylabel("Jumlah sewa sepeda per satu hari")
    st.pyplot(fig)
    with st.expander('See explanation'):
        st.write('Dari hasil analisis data kedua, dapat disimpulkan bahwa Jumlah sepeda yang disewa cenderung lebih banyak ketika hari kerja/ Working Day daripada hari libur/ Holiday')
