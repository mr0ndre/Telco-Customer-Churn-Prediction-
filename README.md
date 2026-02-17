

# Customer Churn Analysis (PLANNING STAGE)

## 1. Project Overview


This project aim to understand why customers choose to discontinue with the service. By using Exploratory Data Analysis (EDA) technique, key factors and patterns that influence churn are identified. Machine Learning models are then implemented to determine whether customers is at "high risk", "moderate risk, "low risk" of churning. 

         
## 2. Business Objective

Customer Churn: 

One of the major concern with businesses is when customers discontinues to use the service provided by the company. This will greatly imact revenue. Understanding the key factors and patterns that lead to customer churn is therefore critical. By analyzing these patterns, businesses can develop retention strategies to maintain healthy revenue streams.  
 

The primary objective of this project is to reduce customer churn by forecasting customers with high risk of leaving, using a machine learning model, and providing actionable recommendations to improve retention.


## 3. Dataset

A fictional telco company that provided home phone and Internet services to 7043 customers in California in Q3, produced by IBM. 


Dataset is retrieved from kaggle: [yeanzc/telco-customer-churn-ibm-dataset](https://www.kaggle.com/datasets/yeanzc/telco-customer-churn-ibm-dataset)

For more details: 
- https://community.ibm.com/community/user/blogs/steven-macko/2019/07/11/telco-customer-churn-1113

### Data Description

The dataset contains 7,043 observations with 33 variables describing customer demographics, service usage, contract information, billing details, and churn-related metrics.

The target variable indicates whether a customer churned during the quarter. Additional variables include customer tenure, contract type, monthly charges, service subscriptions, and customer value metrics such as churn score and customer lifetime value (CLTV).

Feature definitions and dataset documentation are based on the original description provided by the dataset author on Kaggle.

##### Note on Data Usage

The original (raw) dataset is used for exploratory data analysis (EDA) to preserve business-relevant variables and ensure interpretability of insights. However relevant data handling is still applied. 

A separate preprocessed dataset is created for modeling purposes, where certain features are removed or transformed to prevent data leakage, reduce multicollinearity, and improve model performance.

As a result, some variables used in EDA are intentionally excluded from the modeling stage.

============================================================= TO BE CONTINUED ==============================================================




## 6. Key Insights
#### *1. Primary Churn Reasons vs CLTV*
<img width="1184" height="784" alt="image" src="https://github.com/user-attachments/assets/db35d177-ca9f-45e0-82dc-3dfcacaec3d0" />
**Overall insights:**
It appears that the primary factor of customer churning is due to the competitor pressure, they offered better services, more attractive deals, faster speeds, or greater data allowances.

In addition, service quality and customer experience are significant contributors to churn. A noticeable number of customers cited poor support attitudes, lack of professionalism, and unsatisfactory service interactions as reasons for leaving.

Insights for high CLTV customers:
For customers with high CLTV Score, their primary reason to churn is:
         1. Competitor offered more data
         2. Competitor offered higher download speeds 
         3. attitude of support person

This suggests that high-value customers care more about service quality and experience, performance and value relative to competitors. They are willing to change to different providers if the above requirements meet their standard. To retent these customers, overall upgrade to the performance, service attitude and good offers should be considered.

#### *2. Service used by Churn Customers*
<img width="684" height="1184" alt="image" src="https://github.com/user-attachments/assets/3dae3abd-4607-40a6-bac4-5e5180a2df86" />
**Overall insights**

**1. Phone Service:** For those who churned, the most used service is Phone Service. This confirms the findings from previous part, that competitor offered better deals, such as more data for a given plan or in general better offer which attracts them to move.

**2. Streaming & Internet Services**: The second most popular service were the streaming & Internet service.

Fiber optic is the preferred choice for most customers due to its faster speed. Therefore, if a significant number of customers are leaving because of fiber optic speed issues, upgrading network performance must be the company's primary focus

Streaming services (TV and Movies) can be related to internet service if a customer chose both services.
This means that if internet service quality is low, it would also impact Streaming services, and therefore result in much higher chance of customers churning.

#### *3. Tenure Months*
<img width="851" height="1003" alt="image" src="https://github.com/user-attachments/assets/37f0dc61-80de-4e73-873c-9cf5cd147ff4" />
**1. New Customers (< 6 months)**

Finding: Highest churn concentration in first 6 months

Suggestion: Enhance onboarding experience with targeted offers and proactive engagement to improve early retention

**2. Established Customers (> 48 months)**

Finding: Churn among long-term customers indicates potential service quality issues

Suggestion: Implement loyalty rewards, conduct feedback sessions, and prioritize service improvements to retain valuable long-term relationships


## 7. Recommendations


### Key actions to take: 

**1. Upgrade Core Service Performance**
Enhance overall network performance, particularly internet speed and reliability. Improving internet quality would also positively impact related services such as streaming TV and streaming movies.

**2. Strengthen Competitive Offerings**
Introduce more attractive data plans, reduce charges for excess data usage, and periodically benchmark pricing and features against key competitors to remain competitive in the market.

**3. Improve Customer Service Quality**
Provide structured training programs for customer support staff to improve professionalism, communication skills, and service responsiveness. Reducing complaints related to staff attitude will directly improve customer satisfaction and retention.

**4. Close Monitor Customers with Churn Score Above 60**

<img width="545" height="848" alt="image" src="https://github.com/user-attachments/assets/27495bd0-bda1-47ee-8bfb-7dcd11511765" />

Analysis confirms that all churned customers had a churn score between 60 and 100. With zero churned customers falling below this threshold, a score of 60 or higher should be classified as 'High Risk'

Therefore customers with churn score above 60 requires immediate monitoring and targeted intervention to prevent future churn.

### Customer Success & Retention

The majority of retained customers have a tenure exceeding 36 months, indicating that customer loyalty strengthens over time. These long-standing customers represent the company's most valuable asset.

To maintain and strengthen relationships with these loyal customers, we recommend:
**1. Strengthen Customer Relationships:** Develop personalized engagement strategies that make customers feel valued and understood, moving beyond transactional interactions to build emotional connections with the brand.

**2. Implement a Loyalty Rewards Program:** Introduce tiered rewards that acknowledge and appreciate long-term commitment, offering exclusive benefits, discounts, or early access to new features/services.

**3. Establish Continuous Feedback Loops:** Proactively seek customer input through regular surveys, feedback sessions, and advisory panels. Demonstrate that their opinions shape business decisions and service improvements.

**4. Create a "Voice of Customer" Program:** Formally integrate customer feedback into product development and service enhancement cycles, showing customers that their insights drive meaningful change

## 8. Dashboard
Link to your Streamlit dashboard and briefly explain what it shows.
```md
📊 [View Interactive Dashboard](your-streamlit-link)
```

## 9. Models 
Models to forecast if a customer is likely to churn or not
