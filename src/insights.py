def generate_insights(df):
    insights = []

    # Promotion insight
    if "Promo" in df.columns:
        if df["Promo"].iloc[0] == 1:
            insights.append("📈 Promotions are likely boosting sales")

    # Day insight
    if "DayOfWeek" in df.columns:
        day = df["DayOfWeek"].iloc[0]
        if day in [5, 6]:
            insights.append("🔥 Weekend tends to have higher sales")
        else:
            insights.append("📅 Weekday sales pattern observed")

    # Customers insight
    if "Customers" in df.columns:
        if df["Customers"].iloc[0] > 400:
            insights.append("👥 High customer footfall detected")

    return insights