
def project_profit_loss(materials_cost, labor_cost, overhead_cost, projected_savings):
    total_project_cost = materials_cost + labor_cost + overhead_cost
    project_profit_loss = projected_savings - total_project_cost
    project_profit_loss_percent = (project_profit_loss / total_project_cost) * 100
    return total_project_cost, project_profit_loss, project_profit_loss_percent


continueAnalysis = "Y"

while continueAnalysis == "Y":
    materials_cost = float(input("Please enter the materials cost: "))
    labor_cost = float(input("Please enter the labor cost: "))
    overhead_cost = float(input("Please enter the overhead cost: "))
    projected_savings = float(input("Please enter the projected savings or increase in revenue: "))
    total_project_cost, project_profit_loss, project_profit_loss_percent = project_profit_loss(materials_cost, labor_cost, overhead_cost, projected_savings)
    print("Total project cost: ", total_project_cost)
    print("Project profit/loss: ", project_profit_loss)
    print("Project profit/loss as a percent of total cost: ", project_profit_loss_percent)
    continueAnalysis = input("Do you want to analyze another project? (Y/N): ")