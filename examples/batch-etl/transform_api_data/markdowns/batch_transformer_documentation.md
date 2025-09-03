## Transformer block
Now comes the transformer block, the alchemist that refines your data, turning raw information into meaningful insights.

#### How It Works:
**Function Setup**: The transform_data function is enchanted with the @transformer decorator. This magical symbol designates it as the alchemist responsible for enhancing your data within the pipeline.

**Transforming Data**: The function processes each row of the DataFrame, adding a new column serious_event_risk based on the existing cardiac_risk_score. It categorizes each score into risk levels such as 'High risk', 'Medium risk', 'Low risk', or flags them as 'Invalid score' or 'No score' when appropriate.

**Handling Data**: By converting and evaluating the cardiac_risk_score, the transformer ensures that each entry is accurately assessed and categorized. This preparation readies the data for the next stages of your pipeline, enhancing its quality and usefulness.

#### Purpose:
This block acts as the sorcery that elevates your data by analyzing and categorizing cardiac risk scores. It meticulously transforms the raw scores into meaningful risk categories, ensuring that your data is enriched and ready for deeper analysis. With this transformation, your pipeline gains the ability to derive valuable insights from well-structured and categorized data. Click the "Run" button in the transformer block below to witness the transformation.