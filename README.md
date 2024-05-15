#Overview 
House price prediction and personalized house recommendation are important tasks in the real
estate industry, aiding both buyers and sellers in making informed decision. Many real estate
firms have long made decisions based on a combination of intuition and traditional,
retrospective data. Today a host of new variables make it possible to paint more vivid pictures
of location’s future risk and opportunities (Mckinsey,2018).
MagicBricks is a Real Estate company in Canada. Company’s online platform provides deep
coverage of the real estate market and property trends in major cities of Canada. The platform
provides users insights on Tax planning and home loans. The company is expanding its
business in Windsor city. Company recently acquired 110 new properties and will the
predicting the price of those properties. As analysts at the company MagicBricks, we will be
further working for a client to select their dream home. As the client is looking to make the
purchase of house. We will be providing them with through consultation first with the price
prediction and further knowing their preferences or subjective criteria’s we will narrow down
the options of houses that will best suit their requirement.

#Introduction
Real Estate valuation is process to determine the market price of the property. From data driven
decision making to enhanced risk management, increased efficiency, improved customer
service, optimal resource allocation, predictive maintenance and sustainable practices,
Artificial Intelligence algorithms such as Random Forest transforms how real estate projects
are planned and executed. There are various factors that influence the valuation of a property.
(LinkedIn, 2023). Some of the factors include location, size, condition, amenities, and recent
sales of comparable properties in the area. Our data set specific to the area of study includes
total of 546 properties with attributes price, lot size, bedrooms, bathrooms, stories, driveway,
recreation, full base, gas heating, air conditioner and garage.

#Method/ Process
Descriptive Analysis of Data
As observed from summary statistics of data, housing prices in the City of Windsor, ranges
between 25000 and 190000, with an average of 68120. The distribution of sales price is shown
below, which indicates a higher frequency of the houses valued at 50000 and it quickly
decreases after 65000. Some outliers were also observed where the houses were valued at a
higher price than 150000. As the data is from the year 2016, it felt right to improvise the values
by multiplying with 10.

#Visualizing different attributes spread across entire property data.
#Determining the correlation between lot size and price variables.
#Forecasting the price of houses
Random Forest is a supervised machine learning algorithm that is constructed on decision tress
algorithm. It can produce reasonable prediction without hyper-parameter tuning. It can
effectively handle both numerical and categorical features. It has the capabilities to handle
missing values and outliers, which contributes to its robustness.
We used 436 properties as training set and 110 properties as training set. The calculated model
score accuracy is 82%. Please refer to Python workbook for code and statistics.
This study aims to build a predictive model for house prices in the city of Windsor, employing
Random Forest Regression. The dataset includes features such as price, lot size, bedrooms,
bathrooms, stories, driveway, recreation, full basement, gas heating, air conditioning, garage,
and client preference. The following steps outline the process of building the prediction model.

#Data Collection and Preprocessing:
• Gather real estate data for the city of Windsor, including relevant features and target
variable (house prices).
• Check for missing values, outliers, and data inconsistencies.
• Perform data cleaning and imputation as needed.
• Encode categorical variables (e.g., driveway, recreation, full basement) into numerical
representations.
Exploratory Data Analysis (EDA):
• Conduct a comprehensive analysis of the dataset to identify patterns and correlations
between variables.
• Visualize the distribution of house prices and other features.
• Evaluate the impact of different features on house prices using scatter plots, histograms,
and correlation matrices.
Feature Engineering:
• Create new features if relevant to enhance the prediction model's performance.
• Select the most informative features based on correlation analysis and domain
knowledge.

#Data Splitting:
• Divide the dataset into training and testing sets to evaluate the model's generalization
performance accurately.
• Utilize a common ratio, such as 80/20, for the split.
Random Forest Regression Model:
• Implement the Random Forest Regression algorithm, a powerful ensemble learning
technique, to predict house prices.
• Fine-tune hyperparameters, including the number of trees and maximum depth, using
techniques like cross-validation to optimize the model's performance.
Model Training and Evaluation:
• Train the Random Forest Regression model using the training dataset.
• Evaluate the model's performance on the testing dataset using metrics such as Mean
Squared Error (MSE), R-squared (R2), and Mean Absolute Error (MAE).
Model Interpretation:
• Analyze the importance of different features in the prediction process.
• Visualize feature importance using plots, such as bar charts or heatmaps.

#Prediction and Recommendation:
• Utilize the final trained model to predict house prices for newly acquired properties in
the city of Windsor.
• Present the predictions along with confidence intervals for clients' consideration.
Through the systematic implementation of these steps, the built Random Forest Regression
model will provide valuable insights into house prices in Windsor, supporting MagicBricks in
making informed decisions and empowering clients with accurate real estate predictions.
Client’s requirement: MagicBrick’s client wanted a house which costed no more than 900,000
and is a one-story house. Out the 110 properties only 5 properties qualified this requirement.

##Personalized Home Recommendation
All 5 properties have different attributes. It is important to understand what attributes carried
more weight or preference for our client. Selecting one best property out of 5 evolves
multicriteria driven decision making. Hence, we will be using Analytical Hierarchy Process to
achieve this goal.

AHP Process: Analytical Hierarchy Process is multi criteria driven process invented by Thomas
L. Satty in 1970s. It is structured methodology that works through pairwise comparison of
6 qualitative and quantitative evaluation criteria and uses the priority scales driven by expert
judgement for comparison of intangible factors in the evaluation criteria.
Following steps outline the procedure we used AHP to reach our goal to select the best home
for our client.
1. Determine the criteria (and sub-criteria) if any to evaluate.
2. Develop the decision hierarchy with the decision goal (find a best home) at the top,
various alternatives (Property 1-5) at the bottom and various evaluation criteria (Price,
bedrooms, bathroom, etc.) in the middle.
3. Perform the analysis.
    • Perform pairwise comparison of the alternatives (Property 1 -5) based on their
    strengths in meeting the evaluation criteria and determine priorities among
    them.
    • Perform pairwise comparison of the criteria(Price, bedrooms, bathroom, etc.)
    and sub-criteria’s (size of bedroom, garage etc.) based on their importance in
    achieving the goal of the decision-making and determine priorities among them.
4. Synthesize the priorities from steps 2 and 3 to find the overall priority for each of the
alternatives and assign a rank to each of the alternatives on the basis of its overall
priority.
5. Make a decision by selecting the highest ranking alternative.

#Proposed AHP Model
Analysis
To perform the analysis of strength of various alternatives we gave a survey form to the client
to rate each alternative with respect to each other on scale of 1 to 9. We used Saaty’ Scale to
determine the importance of each rating.
Selecting an ideal home
Price Size
Bedrooms
Bathrooms Amenities
Number of
bedrooms
Size of
bedrooms
Closet Space
Living Space
Garden Size
Driveway
Garage
Air
condition
Gas Heat
Property1 Property2 Property3 Property4 Property5
8
Consistency Ratio
The Analytical Hierarchy Process (AHP) utilizes the consistency ratio (CR) to assess the
reliability of pairwise comparisons made by decision-makers. The CR is calculated using the
following formulas:
Consistency Index (CI): CI = (𝝀𝒎𝒂𝒙 - n) / (n - 1)
(where 𝝀𝒎𝒂𝒙 is the principal eigenvalue of the pairwise comparison matrix, and n is the number
of elements being compared)
Random Index (RI): Pre-determined values based on the number of elements being compared.
CR = (CI) / (RI)
If CR exceeds a predefined threshold (typically 0.10), it indicates inconsistency in judgments,
requiring a reassessment to ensure more dependable and accurate decision-making.
Consistency in AHP is critical for producing robust and reliable results, guiding decision-
makers to make well-informed choices based on consistent priorities.
Synthesis and Ranking
We used Python libraries to solve our problem statement. Please refer to Python Workbook for
detailed code. Here, we are explaining each step of AHP process with result snippets from our
Python Workbook.
Goal: To select the ideal home for our client out of 5 alternative properties.
Step 1. Defining criteria and sub-criteria.
Criteria Sub-Criteria
Price None
Bathrooms None
9
Bedrooms
Number of Bedrooms
Size of Bedrooms
Closet Space
Size Living Space
Garden Area
Amenities
Driveway
Garage
Air Conditioning
Gas Heat
Step 2. Normalized Pairwise comparison of criteria & sub-criteria and priority eigen
values.

Step 3: Compute the consistency ratio of the normalized matrix to ensure consistency.
The Consistency Index is: 0.048
The Consistency Ratio is: 0.043
The model is consistent
11
Step 4: Calculate the global weights of the criteria and sub-criteria as per the local
weights.
Step 5: Normalized Pairwise comparison of alternatives with respect to criteria and sub-
criteria and priority eigen values.
13
14
15
16
17
18
19
20
Step 6: Calculating the sum of the global weights of the different alternatives present in
the evoked set.
21
Step 7: Assign rank to each alternative based upon the priority level.
Step 8: As per our decision, Property 3 is best out of 5 other alternatives.


##Conclusion: To summarize, the conjunction of random forest algorithm and analytical
hierarchy method have been beneficial to address this company case. Whether it is predicting
house price accurately or offering personalized house recommendation, this combined
approach has unleashed the true potential of real estate analytics.

