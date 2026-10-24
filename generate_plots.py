import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import os

# Ensure output directory exists
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)

# ============================================
# Plot 1: Monthly Sales Performance (Line Chart)
# ============================================

# Generate sample data
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", 
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
sales = [120, 150, 180, 170, 200, 250, 
         280, 260, 300, 320, 350, 400]

# Create line chart
fig1 = px.line(
    x=months, 
    y=sales,
    markers=True,
    title="Monthly Sales Performance",
    labels={"x": "Month", "y": "Sales ($)"}
)

# Customize the line chart appearance
fig1.update_traces(
    line_color="#2563eb",
    line_width=3,
    marker=dict(size=10, color="#2563eb")
)

fig1.update_layout(
    font_family="Arial",
    title_font_size=20,
    plot_bgcolor="white",
    xaxis=dict(showgrid=True, gridcolor="#e5e7eb"),
    yaxis=dict(showgrid=True, gridcolor="#e5e7eb"),
    hovermode="x unified"
)

# Save as standalone HTML with Plotly.js embedded
fig1.write_html(
    os.path.join(output_dir, "sales_trend.html"),
    include_plotlyjs=True,
    full_html=True
)

# ============================================
# Plot 2: Product Category Distribution (Bar Chart)
# ============================================

# Generate sample data
categories = ["Electronics", "Clothing", "Home & Garden", "Sports", "Books"]
revenue = [45000, 32000, 28000, 19000, 15000]

# Create bar chart
fig2 = go.Figure()

fig2.add_trace(go.Bar(
    x=categories,
    y=revenue,
    marker_color="#f59e0b",
    text=revenue,
    textposition="auto",
    hovertemplate="<b>%{x}</b><br>Revenue: $%{y:,.0f}<extra></extra>"
))

# Customize the bar chart appearance
fig2.update_layout(
    title={
        "text": "Product Category Distribution",
        "font": {"size": 20, "family": "Arial"}
    },
    font_family="Arial",
    plot_bgcolor="white",
    xaxis=dict(
        title="Category",
        showgrid=False
    ),
    yaxis=dict(
        title="Revenue ($)",
        showgrid=True,
        gridcolor="#e5e7eb"
    ),
    hovermode="closest"
)

# Save as standalone HTML with Plotly.js embedded
fig2.write_html(
    os.path.join(output_dir, "category_distribution.html"),
    include_plotlyjs=True,
    full_html=True
)

print("✓ Generated sales_trend.html (Line Chart)")
print("✓ Generated category_distribution.html (Bar Chart)")
print(f"✓ Output directory: {output_dir}/")
