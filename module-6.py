# add additional formatting and logic.

materialCostList = []
laborCostList = []
overheadCostList = []
projectBenefitList = []
print('Project Analysis Program')
print('For MIS525')
print('February 2023 Session')
print('By Student Name')

continueAnalysis = 'Y'
while continueAnalysis == 'Y':
    materialCostList.append(float(input('Enter Material Cost: ')))
    laborCostList.append(float(input('Enter Labor Cost: ')))
    overheadCostList.append(float(input('Enter Overhead Cost: ')))
    projectBenefitList.append(float(input('Enter Projected Benefit: ')))
    continueAnalysis = input('Would you like to enter another project? (Y/N): ').upper()

# Sort the project return list in descending order
projectReturnList = []
for i in range(len(materialCostList)):
    totalProjectCost = materialCostList[i] + (laborCostList[i] + overheadCostList[i])
    projectProfit = projectBenefitList[i] - totalProjectCost
    projectReturn = projectProfit / totalProjectCost
    projectReturnList.append(projectReturn)

sortedIndexList = sorted(range(len(projectReturnList)), key=lambda k: projectReturnList[k], reverse=True)

for i in sortedIndexList:
    totalProjectCost = materialCostList[i] + (laborCostList[i] + overheadCostList[i])
    projectProfit = projectBenefitList[i] - totalProjectCost
    projectProfitPercent = projectProfit / totalProjectCost
    print('========================================')
    print('--- Summary Report for Project ' + str(i + 1))
    print('Prepared by: John Doe')
    print('Material Cost: ' + str(materialCostList[i]))
    print('Labor Cost: ' + str(laborCostList[i]))
    print('Overhead Cost: ' + str(overheadCostList[i]))
    print('Total Cost: ' + str(totalProjectCost))
    print('Cost Savings or Revenue Increase: ' + str(projectBenefitList[i]))
    print('Project Profit: ' + str(projectProfit))
    print('Project Return: {:.2%}'.format(projectProfitPercent))
    if projectProfitPercent < 0:
        print('Interpretation: Project not recommended for approval.')
    elif projectProfitPercent == 0:
        print('Interpretation: Neutral')
    elif projectProfitPercent <= 0.05:
        print('Interpretation: Recommended for approval.')
    else:
        print('Interpretation: Highly recommended for approval.')