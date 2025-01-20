from fastapi import APIRouter, Query
from app.ingestion import load_sales_data
from app.gemini_integration import analyze_sales_with_gemini

router = APIRouter()

# File path for sales data
DATA_FILE_PATH = "data/sales_performance_data.csv"



@router.get("/api/rep_performance")
def get_rep_performance(rep_id: str):
    """
    Analyze the performance of an individual sales representative.
    """
    sales_data = load_sales_data(DATA_FILE_PATH)
    
    # Check if data is extracting
    print("Extracted Sales Data:", sales_data)  # This will print the data to the console
    
    if isinstance(sales_data, dict) and "error" in sales_data:
        return sales_data
    query = f"Provide an in-depth performance review for sales representative {rep_id}. Focus on key metrics like conversion rates and revenue. "
    feedback = analyze_sales_with_gemini(query)
    return {"rep_id": rep_id, "feedback": feedback}

@router.get("/api/team_performance")
def get_team_performance():
    """
    Summarize the overall performance of the sales team.
    """
    sales_data = load_sales_data(DATA_FILE_PATH)
    if isinstance(sales_data, dict) and "error" in sales_data:
        return sales_data
    query = "Summarize the team's overall performance. Identify top performers and areas for improvement."
    feedback = analyze_sales_with_gemini(query)
    if isinstance(feedback, dict) and "error" in feedback:
        return {"error": feedback["error"]}
    return {"team_feedback": feedback}

@router.get("/api/performance_trends")
def get_performance_trends(time_period: str = Query(...)):
    """
    Analyze sales trends over a specific time period.
    """
    sales_data = load_sales_data(DATA_FILE_PATH)
    if isinstance(sales_data, dict) and "error" in sales_data:
        return sales_data
    query = f"Analyze sales trends for the {time_period} and predict future performance."
    feedback = analyze_sales_with_gemini(query)
    return {"time_period": time_period, "trends_feedback": feedback}
