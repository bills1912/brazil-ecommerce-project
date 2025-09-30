import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import folium
from folium.plugins import HeatMap
from streamlit_folium import folium_static
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Olist E-Commerce Dashboard",
    page_icon="🛒",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .main-header {
        font-size: 42px;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 30px;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #1f77b4;
    }
    </style>
""", unsafe_allow_html=True)

# Load data
def load_data():
    """Load all necessary datasets"""
    try:
        orders_df = pd.read_csv('https://raw.githubusercontent.com/bills1912/brazil-ecommerce-project/refs/heads/main/dashboard/dashboard_data/orders_complete.csv')
        rfm_df = pd.read_csv('https://raw.githubusercontent.com/bills1912/brazil-ecommerce-project/refs/heads/main/dashboard/dashboard_data/rfm_analysis.csv')
        monthly_sales = pd.read_csv('https://raw.githubusercontent.com/bills1912/brazil-ecommerce-project/refs/heads/main/dashboard/dashboard_data/monthly_sales.csv')
        delivery_df = pd.read_csv('https://raw.githubusercontent.com/bills1912/brazil-ecommerce-project/refs/heads/main/dashboard/dashboard_data/delivery_performance.csv')
        state_summary = pd.read_csv('https://raw.githubusercontent.com/bills1912/brazil-ecommerce-project/refs/heads/main/dashboard/dashboard_data/state_summary.csv')
        city_summary = pd.read_csv('https://raw.githubusercontent.com/bills1912/brazil-ecommerce-project/refs/heads/main/dashboard/dashboard_data/city_summary.csv')
        category_summary = pd.read_csv('https://raw.githubusercontent.com/bills1912/brazil-ecommerce-project/refs/heads/main/dashboard/dashboard_data/category_summary.csv')
        payment_summary = pd.read_csv('https://raw.githubusercontent.com/bills1912/brazil-ecommerce-project/refs/heads/main/dashboard/dashboard_data/payment_summary.csv')
        
        # Optional files
        try:
            customers_geo = pd.read_csv('https://raw.githubusercontent.com/bills1912/brazil-ecommerce-project/refs/heads/main/dashboard/dashboard_data/customers_with_coordinates.csv')
            product_pairs = pd.read_csv('https://raw.githubusercontent.com/bills1912/brazil-ecommerce-project/refs/heads/main/dashboard/dashboard_data/product_pairs.csv')
            review_summary = pd.read_csv('https://raw.githubusercontent.com/bills1912/brazil-ecommerce-project/refs/heads/main/dashboard/dashboard_data/review_summary.csv')
        except:
            customers_geo = None
            product_pairs = None
            review_summary = None
        
        # Convert datetime columns
        orders_df['order_purchase_timestamp'] = pd.to_datetime(orders_df['order_purchase_timestamp'])
        
        return orders_df, rfm_df, monthly_sales, delivery_df, state_summary, city_summary, category_summary, payment_summary, customers_geo, product_pairs, review_summary
    except FileNotFoundError as e:
        st.error(f"⚠️ Data files not found: {e}")
        st.stop()

# Load data
orders_df, rfm_df, monthly_sales, delivery_df, state_summary, city_summary, category_summary, payment_summary, customers_geo, product_pairs, review_summary = load_data()

# Sidebar
st.sidebar.image("https://img.icons8.com/color/96/000000/shopping-cart.png", width=100)
st.sidebar.title("🛒 Navigation")
page = st.sidebar.radio(
    "Select Page",
    ["📊 Overview", "📈 Sales Analysis", "🗺️ Geographic Analysis", "👥 Customer Analysis", 
     "🚚 Delivery Performance", "🎯 RFM Segmentation", "🔗 Cross-Selling"]
)

st.sidebar.markdown("---")
st.sidebar.markdown("### About")
st.sidebar.info(
    "**Brazilian E-Commerce Dashboard**\n\n"
    "Comprehensive analysis of Olist e-commerce data:\n"
    "- Sales trends and patterns\n"
    "- Geographic distribution & heatmap\n"
    "- Customer segmentation (RFM)\n"
    "- Delivery performance\n"
    "- Cross-selling opportunities\n\n"
    "**Data Period**: 2016-2018"
)

# Main content
if page == "📊 Overview":
    st.markdown('<div class="main-header">🛒 Olist E-Commerce Analytics Dashboard</div>', unsafe_allow_html=True)
    st.markdown("### Business Intelligence Overview")
    
    # Key metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        total_orders = orders_df['order_id'].nunique()
        st.metric("Total Orders", f"{total_orders:,}")
    
    with col2:
        total_revenue = orders_df['payment_value'].sum()
        st.metric("Total Revenue", f"R$ {total_revenue:,.2f}")
    
    with col3:
        total_customers = orders_df['customer_unique_id'].nunique()
        st.metric("Total Customers", f"{total_customers:,}")
    
    with col4:
        avg_order_value = orders_df['payment_value'].mean()
        st.metric("Avg Order Value", f"R$ {avg_order_value:,.2f}")
    
    st.markdown("---")
    
    # Two columns layout
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 📦 Top 10 Product Categories")
        top_10 = category_summary.head(10)
        fig = px.bar(
            top_10,
            x='total_orders',
            y='category',
            orientation='h',
            labels={'total_orders': 'Number of Orders', 'category': 'Category'},
            color='total_orders',
            color_continuous_scale='Viridis'
        )
        fig.update_layout(showlegend=False, height=400, yaxis={'categoryorder': 'total ascending'})
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown("#### 💰 Revenue by Category")
        top_10_revenue = category_summary.nlargest(10, 'total_revenue')
        fig = px.bar(
            top_10_revenue,
            x='total_revenue',
            y='category',
            orientation='h',
            labels={'total_revenue': 'Revenue (R$)', 'category': 'Category'},
            color='total_revenue',
            color_continuous_scale='Reds'
        )
        fig.update_layout(showlegend=False, height=400, yaxis={'categoryorder': 'total ascending'})
        st.plotly_chart(fig, use_container_width=True)
    
    # Geographic overview
    st.markdown("#### 🗺️ Geographic Distribution - Top States")
    top_states = state_summary.head(10)
    
    fig = make_subplots(
        rows=1, cols=2,
        subplot_titles=('Orders by State', 'Revenue by State'),
        specs=[[{'type': 'bar'}, {'type': 'bar'}]]
    )
    
    fig.add_trace(
        go.Bar(x=top_states['state'], y=top_states['total_orders'], 
               name='Orders', marker_color='skyblue'),
        row=1, col=1
    )
    
    fig.add_trace(
        go.Bar(x=top_states['state'], y=top_states['total_revenue'], 
               name='Revenue', marker_color='lightcoral'),
        row=1, col=2
    )
    
    fig.update_layout(height=400, showlegend=False)
    st.plotly_chart(fig, use_container_width=True)
    
    # Monthly trend
    st.markdown("#### 📅 Sales Trend Over Time")
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    
    fig.add_trace(
        go.Scatter(
            x=monthly_sales['year_month'],
            y=monthly_sales['order_id'],
            name="Orders",
            mode='lines+markers',
            line=dict(color='blue', width=3)
        ),
        secondary_y=False
    )
    
    fig.add_trace(
        go.Scatter(
            x=monthly_sales['year_month'],
            y=monthly_sales['payment_value'],
            name="Revenue (R$)",
            mode='lines+markers',
            line=dict(color='red', width=3)
        ),
        secondary_y=True
    )
    
    fig.update_xaxes(title_text="Month")
    fig.update_yaxes(title_text="Number of Orders", secondary_y=False)
    fig.update_yaxes(title_text="Revenue (R$)", secondary_y=True)
    fig.update_layout(height=400, hovermode='x unified')
    
    st.plotly_chart(fig, use_container_width=True)

elif page == "📈 Sales Analysis":
    st.markdown('<div class="main-header">📈 Sales Trend Analysis</div>', unsafe_allow_html=True)
    
    # Date range filter
    st.sidebar.markdown("### Filters")
    date_min = pd.to_datetime(orders_df['order_purchase_timestamp']).min()
    date_max = pd.to_datetime(orders_df['order_purchase_timestamp']).max()
    
    date_range = st.sidebar.date_input(
        "Select Date Range",
        value=(date_min, date_max),
        min_value=date_min,
        max_value=date_max
    )
    
    # Filter data
    if len(date_range) == 2:
        mask = (orders_df['order_purchase_timestamp'] >= pd.to_datetime(date_range[0])) & \
               (orders_df['order_purchase_timestamp'] <= pd.to_datetime(date_range[1]))
        filtered_df = orders_df[mask]
    else:
        filtered_df = orders_df
    
    # KPIs for filtered period
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Orders", f"{filtered_df['order_id'].nunique():,}")
    with col2:
        st.metric("Revenue", f"R$ {filtered_df['payment_value'].sum():,.2f}")
    with col3:
        st.metric("Avg Order Value", f"R$ {filtered_df['payment_value'].mean():,.2f}")
    
    st.markdown("---")
    
    # Category analysis
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🏆 Best Performing Categories")
        cat_dist = filtered_df['product_category_name_english'].value_counts().head(10)
        fig = px.pie(
            values=cat_dist.values,
            names=cat_dist.index,
            title="Top 10 Categories"
        )
        fig.update_traces(textposition='inside', textinfo='percent+label')
        fig.update_layout(height=500)
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown("### 💵 Price Distribution")
        fig = px.histogram(
            filtered_df,
            x='price',
            nbins=50,
            title="Product Price Distribution",
            labels={'price': 'Price (R$)', 'count': 'Frequency'}
        )
        fig.add_vline(
            x=filtered_df['price'].median(),
            line_dash="dash",
            line_color="red",
            annotation_text=f"Median: R$ {filtered_df['price'].median():.2f}"
        )
        fig.update_layout(height=500)
        st.plotly_chart(fig, use_container_width=True)
    
    # Payment methods
    st.markdown("### 💳 Payment Methods")
    fig = px.pie(
        payment_summary,
        values='total_orders',
        names='payment_type',
        title="Payment Type Distribution"
    )
    fig.update_traces(textposition='inside', textinfo='percent+label')
    st.plotly_chart(fig, use_container_width=True)

elif page == "🗺️ Geographic Analysis":
    st.markdown('<div class="main-header">🗺️ Geographic Distribution Analysis</div>', unsafe_allow_html=True)
    
    # Top metrics
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total States", len(state_summary))
    with col2:
        top_state = state_summary.iloc[0]
        st.metric(f"Top State: {top_state['state']}", f"{top_state['total_orders']:,} orders")
    with col3:
        concentration = (state_summary.head(3)['total_orders'].sum() / state_summary['total_orders'].sum()) * 100
        st.metric("Top 3 States Concentration", f"{concentration:.1f}%")
    
    st.markdown("---")
    
    # State comparison
    st.markdown("### 📊 State-Level Analysis")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Top 15 states by orders
        top_15_states = state_summary.head(15)
        fig = px.bar(
            top_15_states,
            x='total_orders',
            y='state',
            orientation='h',
            title="Top 15 States by Orders",
            labels={'total_orders': 'Number of Orders', 'state': 'State'},
            color='total_orders',
            color_continuous_scale='Blues'
        )
        fig.update_layout(height=600, yaxis={'categoryorder': 'total ascending'})
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Top 15 states by revenue
        top_15_revenue = state_summary.nlargest(15, 'total_revenue')
        fig = px.bar(
            top_15_revenue,
            x='total_revenue',
            y='state',
            orientation='h',
            title="Top 15 States by Revenue",
            labels={'total_revenue': 'Revenue (R$)', 'state': 'State'},
            color='total_revenue',
            color_continuous_scale='Reds'
        )
        fig.update_layout(height=600, yaxis={'categoryorder': 'total ascending'})
        st.plotly_chart(fig, use_container_width=True)
    
    # City analysis
    st.markdown("### 🏙️ Top Cities")
    top_20_cities = city_summary.head(20)
    
    fig = px.treemap(
        top_20_cities,
        path=['state', 'city'],
        values='total_orders',
        color='total_revenue',
        title="Top 20 Cities - Orders & Revenue",
        color_continuous_scale='Viridis'
    )
    fig.update_layout(height=600)
    st.plotly_chart(fig, use_container_width=True)
    
    # Heatmap
    if customers_geo is not None and not customers_geo.empty:
        st.markdown("### 🗺️ Customer Distribution Heatmap")
        
        st.info("💡 This map shows the geographic distribution of customers across Brazil. Darker/denser areas indicate higher customer concentration.")
        
        # Sample data for performance (max 5000 points)
        sample_size = min(5000, len(customers_geo))
        geo_sample = customers_geo.dropna(subset=['geolocation_lat', 'geolocation_lng']).sample(n=sample_size, random_state=42)
        
        # Create folium map
        m = folium.Map(
            location=[-14.2350, -51.9253],
            zoom_start=4,
            tiles='OpenStreetMap'
        )
        
        # Prepare heatmap data
        heat_data = [[row['geolocation_lat'], row['geolocation_lng']] 
                     for idx, row in geo_sample.iterrows()]
        
        # Add heatmap
        HeatMap(heat_data, radius=15, blur=25, max_zoom=13).add_to(m)
        
        # Display map
        folium_static(m, width=1200, height=600)
        
        st.caption(f"Showing {sample_size:,} customer locations (sampled from total)")
    else:
        st.warning("Geographic coordinate data not available for heatmap visualization.")

elif page == "👥 Customer Analysis":
    st.markdown('<div class="main-header">👥 Customer Insights & Behavior</div>', unsafe_allow_html=True)
    
    # Customer metrics
    col1, col2, col3 = st.columns(3)
    
    with col1:
        repeat_customers = rfm_df[rfm_df['frequency'] > 1].shape[0]
        repeat_rate = (repeat_customers / len(rfm_df)) * 100
        st.metric("Repeat Customer Rate", f"{repeat_rate:.2f}%")
    
    with col2:
        avg_frequency = rfm_df['frequency'].mean()
        st.metric("Avg Orders per Customer", f"{avg_frequency:.2f}")
    
    with col3:
        customer_lifetime_value = rfm_df['monetary'].mean()
        st.metric("Avg Customer Lifetime Value", f"R$ {customer_lifetime_value:.2f}")
    
    st.markdown("---")
    
    # RFM Distribution
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("### 📊 Recency Distribution")
        fig = px.histogram(
            rfm_df,
            x='recency',
            nbins=50,
            labels={'recency': 'Days Since Last Purchase'},
            color_discrete_sequence=['#636EFA']
        )
        fig.add_vline(
            x=rfm_df['recency'].median(),
            line_dash="dash",
            line_color="red"
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown("### 🔄 Frequency Distribution")
        fig = px.histogram(
            rfm_df,
            x='frequency',
            nbins=20,
            labels={'frequency': 'Number of Orders'},
            color_discrete_sequence=['#00CC96']
        )
        fig.add_vline(
            x=rfm_df['frequency'].median(),
            line_dash="dash",
            line_color="red"
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col3:
        st.markdown("### 💰 Monetary Distribution")
        fig = px.histogram(
            rfm_df,
            x='monetary',
            nbins=50,
            labels={'monetary': 'Total Spending (R$)'},
            color_discrete_sequence=['#EF553B']
        )
        fig.add_vline(
            x=rfm_df['monetary'].median(),
            line_dash="dash",
            line_color="red"
        )
        st.plotly_chart(fig, use_container_width=True)
    
    # Customer by state
    st.markdown("### 🗺️ Customer Distribution by State")
    customer_by_state = state_summary.nlargest(15, 'total_customers')
    
    fig = px.bar(
        customer_by_state,
        x='total_customers',
        y='state',
        orientation='h',
        labels={'total_customers': 'Number of Customers', 'state': 'State'},
        color='total_customers',
        color_continuous_scale='Greens'
    )
    fig.update_layout(height=500, showlegend=False, yaxis={'categoryorder': 'total ascending'})
    st.plotly_chart(fig, use_container_width=True)
    
    # Review distribution
    if review_summary is not None:
        st.markdown("### ⭐ Customer Review Scores")
        fig = px.bar(
            review_summary,
            x='review_score',
            y='count',
            labels={'review_score': 'Review Score', 'count': 'Number of Reviews'},
            color='review_score',
            color_continuous_scale='RdYlGn'
        )
        fig.update_layout(height=400)
        st.plotly_chart(fig, use_container_width=True)
        
        avg_score = (review_summary['review_score'] * review_summary['count']).sum() / review_summary['count'].sum()
        st.info(f"📊 Average Review Score: {avg_score:.2f} / 5.0")

elif page == "🚚 Delivery Performance":
    st.markdown('<div class="main-header">🚚 Delivery Performance Analysis</div>', unsafe_allow_html=True)
    
    # Key delivery metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        avg_delivery_time = delivery_df['actual_delivery_time'].mean()
        st.metric("Avg Delivery Time", f"{avg_delivery_time:.1f} days")
    
    with col2:
        on_time_rate = (delivery_df['on_time'].sum() / len(delivery_df)) * 100
        st.metric("On-Time Delivery Rate", f"{on_time_rate:.1f}%")
    
    with col3:
        early_rate = ((delivery_df['delivery_diff'] > 0).sum() / len(delivery_df)) * 100
        st.metric("Early Deliveries", f"{early_rate:.1f}%")
    
    with col4:
        late_rate = ((delivery_df['delivery_diff'] < 0).sum() / len(delivery_df)) * 100
        st.metric("Late Deliveries", f"{late_rate:.1f}%", delta=f"-{late_rate:.1f}%", delta_color="inverse")
    
    st.markdown("---")
    
    # Delivery time distributions
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 📦 Actual vs Estimated Delivery Time")
        fig = go.Figure()
        fig.add_trace(go.Histogram(
            x=delivery_df['actual_delivery_time'],
            name='Actual Delivery Time',
            opacity=0.7,
            marker_color='blue'
        ))
        fig.add_trace(go.Histogram(
            x=delivery_df['estimated_delivery_time'],
            name='Estimated Delivery Time',
            opacity=0.7,
            marker_color='red'
        ))
        fig.update_layout(
            barmode='overlay',
            xaxis_title='Days',
            yaxis_title='Frequency',
            height=400
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown("### ⏱️ Delivery Time Difference")
        fig = px.histogram(
            delivery_df,
            x='delivery_diff',
            nbins=50,
            labels={'delivery_diff': 'Days (Positive = Early, Negative = Late)'},
            color_discrete_sequence=['#00CC96']
        )
        fig.add_vline(x=0, line_dash="dash", line_color="black", line_width=2)
        fig.update_layout(height=400)
        st.plotly_chart(fig, use_container_width=True)
    
    # On-time delivery pie chart
    st.markdown("### ✅ Delivery Status Distribution")
    col1, col2 = st.columns([2, 1])
    
    with col1:
        on_time_dist = delivery_df['on_time'].value_counts()
        fig = px.pie(
            values=on_time_dist.values,
            names=['On Time / Early', 'Late'],
            color_discrete_sequence=['#00CC96', '#EF553B'],
            hole=0.4
        )
        fig.update_traces(textposition='inside', textinfo='percent+label')
        fig.update_layout(height=400)
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown("#### 📈 Performance Metrics")
        st.metric("Median Actual", f"{delivery_df['actual_delivery_time'].median():.0f} days")
        st.metric("Median Estimated", f"{delivery_df['estimated_delivery_time'].median():.0f} days")
        st.metric("Std Deviation", f"{delivery_df['actual_delivery_time'].std():.1f} days")
        
        # Performance grade
        if on_time_rate >= 95:
            grade = "🏆 Excellent"
        elif on_time_rate >= 90:
            grade = "✅ Good"
        elif on_time_rate >= 85:
            grade = "⚠️ Fair"
        else:
            grade = "❌ Needs Improvement"
        
        st.metric("Performance Grade", grade)

elif page == "🎯 RFM Segmentation":
    st.markdown('<div class="main-header">🎯 RFM Customer Segmentation</div>', unsafe_allow_html=True)
    
    st.markdown("""
    ### What is RFM Analysis?
    **RFM (Recency, Frequency, Monetary)** analysis is a marketing technique used to segment customers based on:
    - **Recency**: How recently a customer made a purchase
    - **Frequency**: How often they purchase
    - **Monetary**: How much money they spend
    """)
    
    # RFM Metrics overview
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("#### 🕐 Recency")
        st.info(f"**Average**: {rfm_df['recency'].mean():.1f} days\n\n**Median**: {rfm_df['recency'].median():.0f} days")
    
    with col2:
        st.markdown("#### 🔄 Frequency")
        st.info(f"**Average**: {rfm_df['frequency'].mean():.2f} orders\n\n**Median**: {rfm_df['frequency'].median():.0f} orders")
    
    with col3:
        st.markdown("#### 💰 Monetary")
        st.info(f"**Average**: R$ {rfm_df['monetary'].mean():.2f}\n\n**Median**: R$ {rfm_df['monetary'].median():.2f}")
    
    st.markdown("---")
    
    # RFM Segment distribution
    if 'segment' in rfm_df.columns:
        st.markdown("### 👥 Customer Segments")
        
        segment_dist = rfm_df['segment'].value_counts()
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            fig = px.pie(
                values=segment_dist.values,
                names=segment_dist.index,
                title="Customer Segment Distribution",
                hole=0.4,
                color_discrete_sequence=px.colors.qualitative.Set3
            )
            fig.update_traces(textposition='inside', textinfo='percent+label')
            fig.update_layout(height=500)
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            st.markdown("#### Segment Details")
            for segment, count in segment_dist.items():
                percentage = (count / len(rfm_df)) * 100
                st.metric(
                    segment,
                    f"{count:,}",
                    f"{percentage:.1f}%"
                )
        
        # RFM scores by segment
        st.markdown("### 📊 RFM Metrics by Segment")
        
        segment_analysis = rfm_df.groupby('segment').agg({
            'recency': 'mean',
            'frequency': 'mean',
            'monetary': 'mean',
            'customer_unique_id': 'count'
        }).round(2)
        segment_analysis.columns = ['Avg Recency (days)', 'Avg Frequency', 'Avg Monetary (R$)', 'Customer Count']
        
        st.dataframe(segment_analysis, use_container_width=True)
        
        # Segment comparison
        col1, col2, col3 = st.columns(3)
        
        with col1:
            fig = px.box(rfm_df, x='segment', y='recency', color='segment',
                        title="Recency by Segment")
            fig.update_layout(showlegend=False, height=400)
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            fig = px.box(rfm_df, x='segment', y='frequency', color='segment',
                        title="Frequency by Segment")
            fig.update_layout(showlegend=False, height=400)
            st.plotly_chart(fig, use_container_width=True)
        
        with col3:
            fig = px.box(rfm_df, x='segment', y='monetary', color='segment',
                        title="Monetary by Segment")
            fig.update_layout(showlegend=False, height=400)
            st.plotly_chart(fig, use_container_width=True)
    
    # Manual Clusters (if available)
    if 'cluster' in rfm_df.columns:
        st.markdown("### 🔍 Manual Customer Clusters")
        
        cluster_labels = {
            0: 'VIP Customers',
            1: 'Loyal Customers',
            2: 'At Risk',
            3: 'Low Value'
        }
        
        cluster_dist = rfm_df['cluster'].value_counts().sort_index()
        
        col1, col2 = st.columns(2)
        
        with col1:
            cluster_names = [cluster_labels.get(i, f'Cluster {i}') for i in cluster_dist.index]
            fig = px.pie(
                values=cluster_dist.values,
                names=cluster_names,
                title="Manual Cluster Distribution",
                color_discrete_sequence=['gold', 'lightblue', 'lightcoral', 'lightgray']
            )
            fig.update_traces(textposition='inside', textinfo='percent+label')
            fig.update_layout(height=400)
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # 3D scatter sample
            sample_size = min(2000, len(rfm_df))
            rfm_sample = rfm_df.sample(n=sample_size, random_state=42)
            
            rfm_sample['cluster_name'] = rfm_sample['cluster'].map(cluster_labels)
            
            fig = px.scatter_3d(
                rfm_sample,
                x='recency',
                y='frequency',
                z='monetary',
                color='cluster_name',
                size='monetary',
                hover_data=['recency', 'frequency', 'monetary'],
                title=f"3D RFM Scatter (Sample: {sample_size})",
                labels={'recency': 'Recency', 'frequency': 'Frequency', 'monetary': 'Monetary'},
                color_discrete_map={
                    'VIP Customers': 'gold',
                    'Loyal Customers': 'lightblue',
                    'At Risk': 'lightcoral',
                    'Low Value': 'lightgray'
                }
            )
            fig.update_layout(height=400)
            st.plotly_chart(fig, use_container_width=True)
    
    # Recommendations
    st.markdown("### 💡 Strategic Recommendations")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.success("""
        **Champions / VIP Customers** 🏆
        - Reward with exclusive offers
        - Request for referrals
        - Premium customer service
        - Early access to new products
        """)
        
        st.info("""
        **Loyal Customers** 🤝
        - Upsell higher value products
        - Encourage reviews and testimonials
        - Special loyalty program
        - Personalized recommendations
        """)
    
    with col2:
        st.warning("""
        **At Risk / Potential Loyalists** ⚠️
        - Re-engagement campaigns
        - Special discount offers
        - Survey to understand concerns
        - Personalized communication
        """)
        
        st.error("""
        **Lost / Low Value** 💔
        - Win-back campaigns
        - Significant incentives
        - Survey for feedback
        - Consider acquisition cost vs LTV
        """)

elif page == "🔗 Cross-Selling":
    st.markdown('<div class="main-header">🔗 Cross-Selling Opportunities</div>', unsafe_allow_html=True)
    
    if product_pairs is not None and not product_pairs.empty:
        st.markdown("### 📦 Frequently Bought Together")
        
        st.info("💡 These product combinations are frequently purchased together in the same order. Use this insight for product bundling, recommendations, and targeted marketing.")
        
        # Top product pairs
        top_pairs = product_pairs.nlargest(15, 'count')
        
        # Create combination label
        top_pairs['combination'] = top_pairs['category_1'] + ' + ' + top_pairs['category_2']
        
        fig = px.bar(
            top_pairs,
            x='count',
            y='combination',
            orientation='h',
            labels={'count': 'Times Bought Together', 'combination': 'Product Combination'},
            color='count',
            color_continuous_scale='Magma',
            title="Top 15 Product Combinations"
        )
        fig.update_layout(height=600, yaxis={'categoryorder': 'total ascending'})
        st.plotly_chart(fig, use_container_width=True)
        
        # Show data table
        st.markdown("### 📋 Product Pair Details")
        display_pairs = product_pairs.nlargest(20, 'count')
        display_pairs = display_pairs.rename(columns={
            'category_1': 'Product Category 1',
            'category_2': 'Product Category 2',
            'count': 'Times Purchased Together'
        })
        st.dataframe(display_pairs, use_container_width=True)
        
        # Cross-selling strategies
        st.markdown("### 💼 Cross-Selling Strategies")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            #### 🎯 Bundling Opportunities
            - Create product bundles based on top combinations
            - Offer discounts for bundle purchases
            - Design "Complete Your Purchase" campaigns
            - Create themed packages (e.g., home office, kitchen essentials)
            """)
            
            st.markdown("""
            #### 📧 Marketing Recommendations
            - Email campaigns: "Customers who bought X also bought Y"
            - Personalized product recommendations
            - Cart recommendations during checkout
            - Post-purchase follow-up suggestions
            """)
        
        with col2:
            st.markdown("""
            #### 🛒 On-Site Recommendations
            - "Frequently bought together" section on product pages
            - Smart shopping cart suggestions
            - "Complete the look/set" recommendations
            - Related products carousel
            """)
            
            st.markdown("""
            #### 📊 Inventory & Merchandising
            - Co-locate related products in warehouse
            - Create combo SKUs for popular pairs
            - Optimize product placement
            - Plan promotional campaigns around pairs
            """)
        
        # Statistics
        st.markdown("### 📈 Cross-Selling Statistics")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            total_pairs = len(product_pairs)
            st.metric("Unique Product Pairs", f"{total_pairs:,}")
        
        with col2:
            avg_count = product_pairs['count'].mean()
            st.metric("Avg Co-Purchases", f"{avg_count:.1f}")
        
        with col3:
            max_count = product_pairs['count'].max()
            st.metric("Most Popular Pair", f"{max_count:,} times")
        
    else:
        st.warning("Product pair data not available. Please run the analysis script to generate cross-selling insights.")
        st.info("Run: `python analisis_data_olist.py` to generate the data.")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; padding: 20px;'>
    <p><b>Olist E-Commerce Analytics Dashboard</b></p>
    <p>Data Analysis Project | Built with Streamlit & Plotly</p>
    <p>📊 Analyzing Brazilian E-Commerce Data (2016-2018)</p>
</div>
""", unsafe_allow_html=True)