import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import networkx as nx

st.set_page_config(page_title="Fraud Detection Dashboard", layout="wide")

st.title("Fraud Detection using Transaction Network Analysis")
st.markdown("Analyze transaction data and detect fraud patterns")

# ---------------- LOAD DATA ----------------
@st.cache_data
def load_data():
    df = pd.read_csv("transactions.csv")

    df = df.dropna()

    df['Date'] = pd.to_datetime(df['Date'])
    df['Hour'] = pd.to_datetime(df['Time']).dt.hour

    return df

df = load_data()

# ---------------- SIDEBAR FILTER ----------------
st.sidebar.header("Filters")

fraud_filter = st.sidebar.selectbox("Fraud", ["All", "Yes", "No"])
type_filter = st.sidebar.selectbox("Type", ["All"] + list(df['Type'].unique()))

filtered_df = df.copy()

if fraud_filter != "All":
    filtered_df = filtered_df[filtered_df['Fraud'] == fraud_filter]

if type_filter != "All":
    filtered_df = filtered_df[filtered_df['Type'] == type_filter]

# ---------------- KPI ----------------
st.subheader("Overview")

col1, col2, col3 = st.columns(3)

col1.metric("Total Transactions", len(filtered_df))
col2.metric("Fraud Transactions", len(filtered_df[filtered_df['Fraud'] == "Yes"]))
col3.metric("Avg Amount", int(filtered_df['Amount'].mean()))

# ---------------- TABS ----------------
tab1, tab2, tab3 = st.tabs(["Analysis", "Network", "Data"])

# ---------------- ANALYSIS ----------------
with tab1:

    # Pie Chart
    fraud_counts = filtered_df['Fraud'].value_counts().reset_index()
    fraud_counts.columns = ['Fraud', 'Count']
    st.plotly_chart(px.pie(fraud_counts, names='Fraud', values='Count',
                           title="Fraud vs Normal"))

    # Histogram
    st.plotly_chart(px.histogram(filtered_df, x="Amount",
                                 title="Transaction Amount Distribution"))

    # Line Graph
    time_series = filtered_df.groupby('Date').size().reset_index(name='Count')
    st.plotly_chart(px.line(time_series, x="Date", y="Count",
                            title="Transactions Over Time"))

    # Bar Chart
    sender_counts = filtered_df['Sender'].value_counts().head(10).reset_index()
    sender_counts.columns = ['Sender', 'Count']
    st.plotly_chart(px.bar(sender_counts, x="Sender", y="Count",
                           title="Top Suspicious Accounts"))

# ---------------- NETWORK GRAPH ----------------
with tab2:

    G = nx.from_pandas_edgelist(filtered_df,
                                source='Sender',
                                target='Receiver',
                                edge_attr='Amount',
                                create_using=nx.Graph())

    pos = nx.spring_layout(G)

    edge_x = []
    edge_y = []

    for edge in G.edges():
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        edge_x.extend([x0, x1, None])
        edge_y.extend([y0, y1, None])

    node_x = []
    node_y = []

    for node in G.nodes():
        x, y = pos[node]
        node_x.append(x)
        node_y.append(y)

    import plotly.graph_objects as go

    fig = go.Figure()

    fig.add_trace(go.Scatter(x=edge_x, y=edge_y,
                             line=dict(width=1),
                             hoverinfo='none',
                             mode='lines'))

    fig.add_trace(go.Scatter(x=node_x, y=node_y,
                             mode='markers+text',
                             text=list(G.nodes()),
                             textposition="top center"))

    fig.update_layout(title="Transaction Network Graph",
                      showlegend=False)

    st.plotly_chart(fig)

# ---------------- DATA ----------------
with tab3:
    st.dataframe(filtered_df)
