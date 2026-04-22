# Deep Learning

[← Back to Main](../README.md)

## Overview

Deep Learning focuses on neural network architectures and training techniques. This section covers DL-specific models (MLP, attention mechanisms, Mamba), architectural patterns (encoders/decoders), generative models (VAE, GANs, diffusion), and advanced training techniques (quantization, distillation, physics-informed learning).

## Deep Learning Models

### Multi-Layer Perceptron (MLP)

![Neural Network Basics](diagrams/neural-network-basics.png)

**Core Concept**: Fully connected feedforward neural networks

- **[Basic MLP](mlp-basics.md)** - Foundational architecture
  - Input layer, hidden layers, output layer
  - Fully connected (dense) layers
  - Non-linear activation functions
  - Universal approximation theorem

- **[Activation Functions](activation-functions.md)** - Non-linearity

| Function | Formula | Range | Gradient | Best For | Issues |
|----------|---------|-------|----------|----------|--------|
| **[ReLU](relu.md)** | max(0, x) | [0, ∞) | 0 or 1 | Hidden layers (default) | Dying ReLU |
| **[Leaky ReLU](leaky-relu.md)** | max(αx, x) | (-∞, ∞) | α or 1 | Avoid dying ReLU | Hyperparameter α |
| **[PReLU](prelu.md)** | max(αx, x) | (-∞, ∞) | Learned | Learn negative slope | More parameters |
| **[ELU](elu.md)** | x if x>0 else α(e^x-1) | (-α, ∞) | Smooth | Faster convergence | Exponential cost |
| **[GELU](gelu.md)** | x·Φ(x) | (-∞, ∞) | Smooth | Transformers, NLP | Slower than ReLU |
| **[Swish](swish.md)** | x·σ(βx) | (-∞, ∞) | Smooth | Deep networks | Slower than ReLU |
| **[Mish](mish.md)** | x·tanh(softplus(x)) | (-∞, ∞) | Smooth | Better than Swish | Slowest |
| **[Sigmoid](sigmoid.md)** | 1/(1+e^-x) | (0, 1) | Vanishing | Output (binary) | Vanishing gradient |
| **[Tanh](tanh.md)** | (e^x-e^-x)/(e^x+e^-x) | (-1, 1) | Vanishing | RNN (legacy) | Vanishing gradient |
| **[Softmax](softmax.md)** | e^xi/Σe^xj | (0, 1), Σ=1 | Varies | Output (multi-class) | Numerical stability |

**Selection Guide**:
- **Default**: ReLU (fast, works well)
- **Transformers/NLP**: GELU
- **Avoid dying neurons**: Leaky ReLU, ELU
- **Deep networks**: Swish, Mish
- **Output layer**: Sigmoid (binary), Softmax (multi-class)

- **[Deep Feedforward Networks](deep-feedforward.md)** - Many-layered MLPs
  - Depth vs width tradeoffs
  - Skip connections
  - Residual connections
  - Highway networks

### Attention Mechanisms

![Transformer Architecture](diagrams/transformer-architecture.png)

**Core Concept**: Dynamic focus on relevant information

| Mechanism | Complexity | Memory | Parallelizable | Best For | Limitations |
|-----------|------------|--------|----------------|----------|-------------|
| **[Self-Attention](self-attention.md)** | O(n²) | O(n²) | Yes | Short sequences | Quadratic cost |
| **[Multi-Head](multi-head-attention.md)** | O(n²) | O(n²) | Yes | Rich representations | More parameters |
| **[Cross-Attention](cross-attention.md)** | O(nm) | O(nm) | Yes | Seq2seq, multimodal | Two sequences needed |
| **[Local Attention](local-attention.md)** | O(nw) | O(nw) | Yes | Long sequences | Limited context |
| **[Sparse Attention](sparse-attention.md)** | O(n√n) | O(n√n) | Partial | Very long sequences | Pattern design |
| **[Flash Attention](flash-attention.md)** | O(n²) | O(n) | Yes | Memory-bound | Hardware-specific |
| **[Linear Attention](linear-attention.md)** | O(n) | O(n) | Yes | Very long sequences | Approximation |

**Attention Variants Comparison**:

| Variant | Pattern | Context | Use Case |
|---------|---------|---------|----------|
| **Full** | All-to-all | Global | Standard Transformer |
| **Local** | Window | Local | Long documents |
| **Strided** | Every k-th | Sparse global | Longformer |
| **Block** | Block diagonal | Structured | BigBird |
| **Random** | Random subset | Approximate global | Sparse Transformer |
| **Axial** | Row + Column | 2D | Images |

### Mamba (State Space Models)

**Core Concept**: Efficient sequence modeling alternative to attention

- **[State Space Models (SSM)](state-space-models.md)** - Linear recurrence
  - Continuous-time formulation
  - Discretization methods
  - Structured matrices
  - Linear time complexity O(n)

- **[Mamba Architecture](mamba.md)** - Selective SSM
  - Input-dependent parameters
  - Selective scan algorithm
  - Hardware-aware implementation
  - Competitive with Transformers

- **[Mamba vs Attention](mamba-vs-attention.md)** - Comparison
  - Computational efficiency
  - Long-range dependencies
  - Training dynamics
  - Use case selection

## Architectural Patterns

### Encoder-Decoder Architectures

| Architecture | Direction | Training | Examples | Best For |
|--------------|-----------|----------|----------|----------|
| **[Encoder-Only](encoder-only.md)** | Bidirectional | Masked LM | BERT, RoBERTa | Classification, NER |
| **[Decoder-Only](decoder-only.md)** | Causal | Next token | GPT family | Text generation |
| **[Encoder-Decoder](encoder-decoder-models.md)** | Both | Seq2seq | T5, BART | Translation, summarization |

### Convolutional Architectures

| Architecture | Innovation | Parameters | Depth | Best For |
|--------------|-----------|------------|-------|----------|
| **[CNN Basics](cnn-basics.md)** | Local connectivity | Low | Shallow | Image features |
| **[ResNet](modern-cnns.md)** | Residual connections | Medium | Very deep (50-152) | Image classification |
| **[DenseNet](modern-cnns.md)** | Dense connections | High | Deep (121-201) | Feature reuse |
| **[EfficientNet](modern-cnns.md)** | Compound scaling | Optimized | Varies | Efficiency |
| **[ConvNeXt](modern-cnns.md)** | Modernized design | Medium | Deep | Competitive with ViT |

### Recurrent Architectures

| Architecture | Gates | Parameters | Memory | Best For | Limitations |
|--------------|-------|------------|--------|----------|-------------|
| **[Vanilla RNN](rnn-basics.md)** | None | Low | Short-term | Simple sequences | Vanishing gradients |
| **[LSTM](lstm.md)** | 3 (forget, input, output) | High | Long-term | Long sequences | Slow training |
| **[GRU](gru.md)** | 2 (reset, update) | Medium | Long-term | Efficient sequences | Less expressive |

## Generative Models

![Generative Models](diagrams/generative-models.png)

### Variational Autoencoders (VAE)

| Variant | Innovation | Latent Space | Training | Best For |
|---------|-----------|--------------|----------|----------|
| **[Vanilla VAE](vae-fundamentals.md)** | ELBO optimization | Continuous Gaussian | Stable | General generation |
| **[β-VAE](vae-variants.md)** | Weighted KL | Disentangled | Stable | Interpretable factors |
| **[CVAE](vae-variants.md)** | Conditional | Conditional | Stable | Controlled generation |
| **[VQ-VAE](vae-variants.md)** | Vector quantization | Discrete codebook | Complex | High-quality images |
| **[Hierarchical VAE](vae-variants.md)** | Multi-level | Hierarchical | Complex | Complex distributions |

### Generative Adversarial Networks (GAN)

| Variant | Innovation | Stability | Quality | Best For |
|---------|-----------|-----------|---------|----------|
| **[Vanilla GAN](gan-fundamentals.md)** | Adversarial training | Low | Medium | Proof of concept |
| **[DCGAN](gan-variants.md)** | Convolutional | Medium | Good | Image generation |
| **[StyleGAN](gan-variants.md)** | Style-based | High | Excellent | High-res faces |
| **[CycleGAN](gan-variants.md)** | Cycle consistency | Medium | Good | Unpaired translation |
| **[Progressive GAN](gan-variants.md)** | Progressive growing | High | Excellent | High-resolution |
| **[BigGAN](gan-variants.md)** | Large-scale | Medium | Excellent | ImageNet scale |

**GAN Training Challenges**:

| Issue | Solution | Complexity | Effectiveness |
|-------|----------|------------|---------------|
| **Mode collapse** | Minibatch discrimination | Medium | Partial |
| **Training instability** | WGAN, Spectral norm | Medium | High |
| **Gradient issues** | Gradient penalty | Low | High |
| **Convergence** | Two time-scale update | Low | Medium |

### Diffusion Models

- **[Diffusion Fundamentals](diffusion-fundamentals.md)** - Denoising process
  - Forward diffusion (noise addition)
  - Reverse diffusion (denoising)
  - Score matching
  - Langevin dynamics

- **[DDPM](ddpm.md)** - Denoising Diffusion Probabilistic Models
  - Markov chain formulation
  - Noise schedule
  - Training objective
  - Sampling process

- **[Latent Diffusion](latent-diffusion.md)** - Efficient diffusion
  - VAE latent space
  - Stable Diffusion
  - Text conditioning
  - Classifier-free guidance

- **[Diffusion Variants](diffusion-variants.md)** - Advanced techniques
  - DDIM (deterministic sampling)
  - Score-based models
  - Consistency models
  - Flow matching

### Other Generative Models

- **[Normalizing Flows](normalizing-flows.md)** - Invertible transformations
  - Exact likelihood
  - Bijective mappings
  - RealNVP, Glow
  - Continuous normalizing flows

- **[Autoregressive Models](autoregressive-models.md)** - Sequential generation
  - PixelCNN, PixelRNN
  - WaveNet
  - Transformer-based (GPT)
  - Parallel generation techniques

## Training Techniques

### Supervised Fine-Tuning (SFT)

| Approach | Parameters Updated | Memory | Training Time | Best For | Risk |
|----------|-------------------|--------|---------------|----------|------|
| **[Full Fine-Tuning](fine-tuning-strategies.md)** | All | High | Long | Maximum adaptation | Catastrophic forgetting |
| **[Layer Freezing](fine-tuning-strategies.md)** | Partial | Medium | Medium | Limited data | Underfitting |
| **[LoRA](peft.md)** | Low-rank matrices | Low | Fast | Efficient adaptation | Limited expressiveness |
| **[Adapter Layers](peft.md)** | Small modules | Low | Fast | Multi-task | Architecture change |
| **[Prefix Tuning](peft.md)** | Soft prompts | Very low | Very fast | Prompt-based tasks | Task-specific |
| **[Prompt Tuning](peft.md)** | Input embeddings | Minimal | Very fast | Few parameters | Limited control |

**Instruction Tuning Benefits**:
- Multi-task generalization across diverse instructions
- Zero-shot and few-shot capabilities
- Better alignment with user intent
- Improved instruction following

### Reinforcement Learning (RL)

| Method | Complexity | Reward Model | Training Stability | Best For | Limitations |
|--------|------------|--------------|-------------------|----------|-------------|
| **[RLHF](rlhf.md)** | High | Yes (trained) | Medium | Human alignment | Complex pipeline |
| **[DPO](dpo.md)** | Medium | No (implicit) | High | Simplified alignment | Preference pairs needed |
| **[REINFORCE](policy-gradient.md)** | Medium | Yes | Low | General RL | High variance |
| **[Actor-Critic](policy-gradient.md)** | High | Yes (critic) | Medium | Stable training | More complex |
| **[PPO](rlhf.md)** | High | Yes | High | Stable policy updates | Hyperparameter sensitive |

**RL Training Considerations**:
- **Reward modeling**: Quality of human feedback critical
- **Exploration**: Balance between exploitation and exploration
- **Stability**: Use clipping, KL penalties for stable training
- **Alignment**: Ensure model behavior matches human values

## Advanced DL Techniques

### Model Compression

| Technique | Compression Ratio | Accuracy Loss | Training Required | Best For | Limitations |
|-----------|------------------|---------------|-------------------|----------|-------------|
| **[Quantization](quantization.md)** | 2-4x | Low | Optional (QAT) | Inference speed | Hardware support needed |
| **[Knowledge Distillation](knowledge-distillation.md)** | Flexible | Low-Medium | Yes (student) | Model size reduction | Requires teacher model |
| **[Pruning](pruning.md)** | 2-10x | Low-Medium | Optional | Sparse models | May need retraining |
| **[Low-Rank Factorization](low-rank.md)** | 2-3x | Low | Optional | Memory reduction | Limited compression |
| **[Weight Sharing](weight-sharing.md)** | 2-4x | Low | Yes | Parameter reduction | Architecture constraints |

**Quantization Methods**:

| Method | Precision | Accuracy | Speed | When to Use |
|--------|-----------|----------|-------|-------------|
| **FP32** | 32-bit | Baseline | 1x | Training, high precision needed |
| **FP16** | 16-bit | ~Same | 2x | Training with mixed precision |
| **INT8** | 8-bit | -1-2% | 3-4x | Inference, post-training |
| **INT4** | 4-bit | -2-5% | 4-6x | LLM inference, memory-bound |
| **Binary** | 1-bit | -10-20% | 8-16x | Extreme compression |

**Distillation Variants**:

| Type | Teacher | Student | Best For |
|------|---------|---------|----------|
| **Response-based** | Soft labels | Any | Classification |
| **Feature-based** | Intermediate layers | Similar architecture | Rich representations |
| **Relation-based** | Feature relationships | Any | Structural knowledge |
| **Self-distillation** | Same model | Same model | Regularization |

### Training Dynamics

- **[Grokking](grokking.md)** - Delayed generalization
  - Memorization to generalization transition
  - Extended training benefits
  - Weight decay effects
  - Phase transitions

- **[Double Descent](double-descent.md)** - Non-monotonic risk
  - Classical bias-variance tradeoff
  - Modern overparameterized regime
  - Interpolation threshold
  - Sample-wise double descent

- **[Neural Tangent Kernel](ntk.md)** - Infinite width limit
  - Kernel regime
  - Lazy training
  - Feature learning
  - Theoretical analysis

### Physics-Informed Neural Networks

- **[PINN Fundamentals](pinn-fundamentals.md)** - Physics constraints
  - PDE residuals in loss
  - Boundary conditions
  - Initial conditions
  - Automatic differentiation

- **[PINN Architectures](pinn-architectures.md)** - Specialized designs
  - Fourier feature networks
  - Multi-scale architectures
  - Adaptive activation functions
  - Domain decomposition

- **[PINN Applications](pinn-applications.md)** - Scientific computing
  - Fluid dynamics
  - Heat transfer
  - Quantum mechanics
  - Inverse problems

## Optimization and Regularization

### Optimizers

| Optimizer | Learning Rate | Momentum | Adaptive | Memory | Best For | Limitations |
|-----------|--------------|----------|----------|--------|----------|-------------|
| **[SGD](sgd.md)** | Fixed/Scheduled | No | No | Low | Simple problems | Slow convergence |
| **[SGD + Momentum](sgd-momentum.md)** | Fixed/Scheduled | Yes | No | Low | General purpose | Hyperparameter tuning |
| **[Nesterov](nesterov.md)** | Fixed/Scheduled | Yes (lookahead) | No | Low | Faster convergence | Similar to momentum |
| **[Adagrad](adagrad.md)** | Adaptive | No | Yes | Medium | Sparse data | Learning rate decay |
| **[RMSprop](rmsprop.md)** | Adaptive | No | Yes | Medium | RNNs | Not well-studied |
| **[Adam](adam.md)** | Adaptive | Yes | Yes | Medium | General purpose | May not converge |
| **[AdamW](adamw.md)** | Adaptive | Yes | Yes | Medium | Transformers, LLMs | Slightly slower |
| **[NAdam](nadam.md)** | Adaptive | Yes (Nesterov) | Yes | Medium | Faster than Adam | More hyperparameters |
| **[RAdam](radam.md)** | Adaptive (rectified) | Yes | Yes | Medium | Stable training | Slower initially |
| **[AdaBound](adabound.md)** | Adaptive→Fixed | Yes | Yes | Medium | Best of both worlds | Complex |
| **[L-BFGS](lbfgs.md)** | Line search | No | No (2nd order) | High | Small batches | Not for large-scale |

**Selection Guide**:
- **Default choice**: AdamW (most robust)
- **Computer Vision**: SGD with momentum (better generalization)
- **NLP/Transformers**: AdamW
- **RNNs**: RMSprop, Adam
- **Sparse data**: Adagrad
- **Stable training**: RAdam
- **Fine-tuning**: AdamW with low LR

### Regularization

- **[Dropout](dropout.md)** - Random deactivation
  - Standard dropout
  - DropConnect
  - Variational dropout
  - Dropout scheduling

- **[Batch Normalization](batch-normalization.md)** - Normalizing activations
  - Internal covariate shift
  - Training vs inference mode
  - Batch size sensitivity
  - Alternatives (Layer Norm, Group Norm)

- **[Data Augmentation](data-augmentation.md)** - Expanding training data
  - Image augmentation (crop, flip, color)
  - Text augmentation (back-translation, paraphrasing)
  - Mixup, CutMix
  - AutoAugment

### Loss Functions

- **[Classification Losses](classification-losses.md)** - Discrete outputs
  - Cross-entropy
  - Focal loss
  - Label smoothing
  - Contrastive loss

- **[Regression Losses](regression-losses.md)** - Continuous outputs
  - MSE (Mean Squared Error)
  - MAE (Mean Absolute Error)
  - Huber loss
  - Quantile loss

## Implementation Frameworks

<div style="color: green;">

### Deep Learning Frameworks
- **PyTorch** - Dynamic computation graphs, research-friendly
- **TensorFlow/Keras** - Production-ready, comprehensive ecosystem
- **JAX** - High-performance, functional programming
- **MXNet** - Efficient, scalable

### Model Libraries
- **Hugging Face Transformers** - Pre-trained models
- **timm** - PyTorch image models
- **torchvision** - Computer vision models
- **torchaudio** - Audio processing

### Training Tools
- **PyTorch Lightning** - Training boilerplate reduction
- **Accelerate** - Distributed training
- **DeepSpeed** - Large model training
- **FSDP** - Fully Sharded Data Parallel

</div>

## Best Practices

### Model Development
1. Start with pre-trained models when available
2. Use appropriate architecture for task
3. Monitor training dynamics (loss curves, gradients)
4. Implement early stopping
5. Use validation set for hyperparameter tuning

### Training Efficiency
- Mixed precision training (FP16/BF16)
- Gradient accumulation for large batches
- Gradient checkpointing for memory
- Efficient data loading (prefetching, caching)
- Profile and optimize bottlenecks

### Debugging
- Check data pipeline first
- Verify loss decreases on small batch
- Monitor gradient norms
- Visualize activations and weights
- Use tensorboard/wandb

## Related Topics

- [Machine Learning](../machine-learning/README.md) - Classical ML models
- [NLP](../modalities/nlp/README.md) - Language-specific techniques
- [Computer Vision](../modalities/vision/README.md) - Vision-specific techniques
- [MLOps](../mlops/README.md) - Model deployment

## Further Learning

<div style="color: green;">

### Books
- "Deep Learning" by Goodfellow, Bengio, Courville
- "Dive into Deep Learning" by Zhang et al.
- "Understanding Deep Learning" by Simon Prince
- "Deep Learning with PyTorch" by Stevens et al.

### Courses
- Stanford CS231n (Computer Vision)
- Stanford CS224n (NLP)
- Fast.ai Practical Deep Learning
- DeepLearning.AI Specialization

### Papers
- "Attention Is All You Need" (Transformers)
- "BERT: Pre-training of Deep Bidirectional Transformers"
- "Denoising Diffusion Probabilistic Models"
- "LoRA: Low-Rank Adaptation of Large Language Models"

### Resources
- Papers with Code
- Distill.pub
- arXiv.org
- Hugging Face Blog

</div>

---

*Deep Learning provides powerful models and techniques for learning complex patterns from raw data across diverse domains.*