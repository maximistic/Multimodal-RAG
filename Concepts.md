Some concepts to know before building the Multimodal RAG:

    - Multimodal can mean:
        - Input and Output are of different modalities (text-to-image or image-to-text or so one)
        - Inputs are multimodal (a system that can process both image and data)
        - Outputs are multimodal (a system that can generate both image and data)
    - Multimodal LLMs combine the capabilities of NLP with other modalities. A brief overview of their structure:
        - An encoder for each data modality to generate the embeddings for data modality
        - A way to align different embeddings of different modalities into the same multimodal embedding space.
        - A Generative language model to generate text responses. 
    - Vision Transformers (ViT) are a type of AI model that can process images.
    - LLM Halucinations - events in which the LLMs produce output that are coherent and grammatically correct but are factually not or nonsensical. These hallucinations are caused due to various factors such as limitations in training data, biases in the model, or inherent complexity of the language.
        - Incomplete or noisy training data
        - Vague questions
        - Overfitting and underfitting
        - Semantic gaps
        - Absence of Grounding
        - Outdated information
    - RAG - provides the methodology by which user can retrieve the relevant document-chunks from the vector-database using vector similarity search and then use these retrieved chunks to generate the final output from the LLM.
    - CRAG (Corrective Retrieval Augmented Generation) - solution which enhances the context information which is retrieved by the retriever  from the vector databases.
    - MuRAGs (Multimodal RAG) are used along with multimodal LLMs, which are used to process images for generating results. 
    