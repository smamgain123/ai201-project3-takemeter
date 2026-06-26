
## Error Analysis

The fine-tuned model got 12 out of 29 test examples wrong. A clear pattern was that the model over-predicted `reaction`, likely because `reaction` was the largest class in the dataset.

### Example 1
Text: "Both sides were unhappy with the KAT/Randle trade initially too. One side can just be overrating their previous player."

True label: `analysis`  
Predicted label: `reaction`

This was labeled as analysis because it compares the current trade discussion to a previous trade and gives reasoning. The model likely predicted reaction because the wording is casual and Reddit-style.

### Example 2
Text: "he was gay, Lamelo Ball?"

True label: `question`  
Predicted label: `reaction`

This is technically a question because it asks something directly, but it also sounds like a meme/reaction. The model likely focused on the short sarcastic style instead of the question mark.

### Example 3
Text: "He must have told the front office to fuck off when they asked him to take a driver's ed course."

True label: `hot_take`  
Predicted label: `reaction`

This is a hot take because it makes a strong unsupported assumption about the player and front office. The model predicted reaction because it is humorous and emotional, which overlaps with the reaction class.

### Takeaway
Most wrong predictions happened because the dataset was imbalanced. The `reaction` label had many more examples than the other labels, so the model learned to predict `reaction` too often. Future improvements would include collecting more `analysis`, `hot_take`, and `question` examples and reviewing borderline labels more carefully.
=======
