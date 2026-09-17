# GEN-AI

## Table of Contents

- [Class-1 (Introduction to Generative AI)](#class-1-introduction-to-generative-ai)
- [Class-2 (Introduction to Generative AI - 2)](#class-2-introduction-to-generative-ai---2)
- [Class-3 (Agents - Real World Applications)](#class-3-agents---real-world-applications)
- [Class-4 (Prompts)](#class-4-prompts)

### Class-1 (Introduction to Generative AI)

- AI was first introduced in 1956 at the Dartmouth Conference, where the term "Artificial Intelligence" was coined. Since then, AI has evolved significantly, leading to the development of various subfields, including Generative AI.
- Generative AI refers to a class of artificial intelligence algorithms that can generate new content, such as images, text, music, and more, based on the data they have been trained on. These models learn patterns and structures from existing data and use that knowledge to create novel outputs.
- Generative AI has gained significant attention in recent years due to its ability to produce creative and realistic content. Some popular applications of Generative AI include:
  - Text Generation: Models like GPT-3 and GPT-4 can generate human-like text based on prompts, enabling applications such as chatbots, content creation, and language translation.
  - Image Generation: Models like DALL-E and StyleGAN can create realistic images from textual descriptions or generate new images based on existing ones.
  - Music Generation: AI models can compose original music pieces by learning from existing compositions, enabling new forms of musical creativity.
  - Video Generation: Generative AI can also be used to create videos, either by generating new video content or enhancing existing footage.
- The underlying techniques used in Generative AI include:
  - Neural Networks: Deep learning models, particularly neural networks, are commonly used in Generative AI. These networks can learn complex patterns and relationships in data, enabling them to generate new content.
  - Variational Autoencoders (VAEs): VAEs are a type of generative model that learns to encode input data into a latent space and then decode it back to generate new samples.
  - Generative Adversarial Networks (GANs): GANs consist of two neural networks, a generator and a discriminator, that compete against each other. The generator creates new content, while the discriminator evaluates its authenticity, leading to improved generation over time.
  - Transformers: Transformer architectures, such as those used in GPT models, have revolutionized natural language processing and generation by enabling models to capture long-range dependencies in text.
- Reinforcement Learning: Some generative models can be trained using reinforcement learning techniques, where the model learns to generate content based on feedback and rewards.
- Generative AI has numerous applications across various industries, including entertainment, healthcare, marketing, and more. It has the potential to revolutionize creative processes, automate content generation, and enhance user experiences.

### Class-2 (Introduction to Generative AI - 2)

- Initially AI was `rule-based`, relying on predefined rules and logic to make decisions. However, with the advent of machine learning, AI systems began to learn from data and improve their performance over time.
- Later `Machine Learning (ML)` emerged as a subfield of AI, focusing on developing algorithms that allow computers to learn from data without being explicitly programmed. ML algorithms can identify patterns, make predictions, and adapt to new information.
- `Deep Learning (DL)` is a subset of ML that utilizes neural networks with multiple layers to model complex relationships in data. DL has been instrumental in advancing Generative AI, enabling the creation of sophisticated models capable of generating high-quality content.

- _LLMs (Large Language Models)_ are a type of deep learning model that has gained significant attention in recent years. These models are trained on vast amounts of text data and can generate coherent and contextually relevant text based on prompts. LLMs have been used in various applications, including chatbots, virtual assistants, and content generation.

- How LLMs work:
  - LLMs are typically based on transformer architectures, which allow them to capture long-range dependencies in text and generate contextually appropriate responses.
  - During training, LLMs learn to predict the next word in a sequence of text, enabling them to generate coherent sentences and paragraphs.
  - LLMs can be fine-tuned on specific tasks or domains, allowing them to specialize in generating content for particular applications.

_Prompt > Knowledge > Memory > Tools_

### Class-3 (Agents - Real World Applications)

- `Intrakat application` and `Make` of Generative AI in real-world scenarios has led to the development of intelligent agents that can perform tasks autonomously and assist users in various domains. These agents leverage the capabilities of Generative AI models to understand user inputs, generate relevant responses, and take actions based on the context.

### Class-4 (Prompts)

- Different Types of Prompts:
  - _Zero-shot prompts_: These prompts provide a task description without any examples, and the model is expected to generate a response based solely on its pre-trained knowledge.
  - _One-shot prompts_: These prompts provide a single example of the desired output, allowing the model to learn from that example and generate a response accordingly.
  - _Few-shot prompts_: These prompts provide multiple examples of the desired output, enabling the model to learn from the examples and generate a response that aligns with the provided context.
  - _Chain-of-thought prompts_: These prompts encourage the model to generate intermediate reasoning steps before arriving at a final answer, allowing for more complex problem-solving and reasoning.
  - _Role-based prompts_: These prompts assign specific roles or personas to the model, guiding its responses based on the assigned role and context.
