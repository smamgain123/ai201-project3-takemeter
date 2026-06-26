# TakeMeter Planning

## Community

I chose r/nba because NBA discussion has many different types of comments. Some comments are detailed basketball analysis, some are emotional reactions, some are bold hot takes, and some are questions. This makes it a good community for a classifier because the discourse is active, text-heavy, and varied.

## Labels

### analysis
A comment that makes a reasoned basketball argument using stats, examples, strategy, or comparison.

Examples:
- "The Lakers struggled because their spacing collapsed whenever AD sat."
- "SGA’s scoring is sustainable because he gets to the line and creates efficient midrange looks."

### hot_take
A bold opinion stated confidently without much supporting evidence.

Examples:
- "This team is never winning a championship."
- "He is the most overrated player in the league."

### reaction
An emotional, funny, or immediate response to a game, play, player, or news.

Examples:
- "NO WAY HE HIT THAT."
- "This game is insane lol."

### question
A comment mainly asking for information, clarification, or discussion.

Examples:
- "Why did they bench him in the fourth?"
- "Is he injured or just resting?"

## Hard Edge Cases

Some comments are both opinionated and analytical. If a comment gives specific basketball reasoning, evidence, or examples, I will label it analysis. If it mostly makes a bold claim without explaining why, I will label it hot_take.

Example:
"LeBron is overrated because his playoff record against top seeds is weak."

This could be analysis or hot_take. I would label it hot_take because the comment uses one broad claim but does not explain the context or build a full argument.

## Data Collection Plan

I will collect at least 200 public Reddit comments from r/nba game threads, post-game threads, and discussion posts. I will aim for about 50 examples per label: analysis, hot_take, reaction, and question. If one label is underrepresented, I will collect more examples for that label.

## Evaluation Metrics

I will use overall accuracy to measure general performance. I will also use per-class F1 score because accuracy alone can hide whether the model is bad at one specific label. The confusion matrix will help show which labels the model confuses.

## Definition of Success

The classifier will be successful if it beats the Groq zero-shot baseline and reaches around 70% accuracy or better. It should also have reasonable per-class F1 scores, meaning it should not completely fail on one label.

## AI Tool Plan

I will use AI tools to stress-test my label definitions by generating borderline examples. I may use AI to help pre-label some examples, but I will manually review and correct every label. After evaluation, I will use AI to help identify patterns in the model’s wrong predictions, but I will verify those patterns myself.