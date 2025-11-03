# Home Visualization Platform - Project Overview

## Project Description
A production-grade AI-powered web platform that enables users to upload home images and visualize different material/texture options in real-time. Built as a scalable microservices architecture using FastAPI, the system integrates multiple ML services for automated house element detection, segmentation, and realistic material replacement.

## Key Features & Functionalities

### 1. AI-Powered Image Segmentation
- **Roboflow Model Integration**: Automated detection and segmentation of house elements (walls, roofs, windows, doors, masonry)
- **Real-time Annotation**: Generates color-coded, labeled masks with confidence scores
- **Support for High-Resolution Images**: Intelligent downscaling and compression for optimal processing
- **Element Classification**: Identifies and categorizes structural components with JSON metadata

### 2. Advanced Material Replacement Engine
- **Multiple Processing Methods**: 
  - CV Poisson blending for realistic texture integration
  - ComfyUI integration for advanced AI-based material replacement
- **Smart Texture Application**:
  - Automatic orientation detection and alignment
  - Element-specific scaling based on size and type
  - Color matching (Reinhard algorithm) for seamless integration
  - Support for fixed or automatic angle rotation
- **Material Library**: Curated catalog with hierarchical material organization
- **Batch Processing**: Replace multiple elements simultaneously with different materials

### 3. User Management & Authentication
- **JWT-based Authentication**: Secure access tokens with refresh mechanism
- **User Registration**: Custom user profiles with company/contractor information
- **Password Management**: Forgot/reset password flow with token-based security
- **Session Management**: Anonymous sessions for non-authenticated users

### 4. Payment Integration (Stripe)
- **Checkout Sessions**: Secure payment processing
- **Webhook Handling**: Real-time payment status updates
- **Transaction History**: Complete audit trail of payments
- **Customer Linking**: Automatic user-payment association

### 5. File Management System
- **Cloud Storage**: Multi-provider support (Cloudinary, AWS S3)
- **Gallery Management**: User-specific image galleries with metadata
- **Staged Upload Flow**: Session-based staging before commit
- **Image Optimization**: Automatic compression and format conversion
- **CDN Delivery**: Fast, global image distribution

### 6. History & Session Tracking
- **Timeline System**: Complete visualization history per user/session
- **Event Logging**: Track segmentation and material replacement operations
- **Latest Snapshot**: Quick access to current visualization state
- **Category-based Queries**: Filter by element type or material

### 7. Product Catalog API
- **Hierarchical Material Database**: Organized by categories (Wall, Roof, Accent, etc.)
- **Dynamic Browsing**: RESTful endpoints for material exploration
- **Image Mapping**: Direct access to material preview images
- **Material Metadata**: Structured product information

### 8. Contact Management
- **Request System**: Contact form submissions
- **Service Layer**: Automated processing and notification workflows

## Technical Stack

### Backend
- **Framework**: FastAPI (async Python web framework)
- **Database**: PostgreSQL with SQLAlchemy ORM
- **Authentication**: JWT tokens with bcrypt password hashing
- **Migrations**: Alembic for database version control

### AI/ML Services
- **Computer Vision**: OpenCV, PIL/Pillow
- **ML Libraries**: PyTorch, Roboflow, HuggingFace Hub
- **Segmentation**: Supervision library for annotation
- **External APIs**: ComfyUI, Roboflow model inference

### Cloud & Storage
- **CDN**: Cloudinary for image delivery
- **Object Storage**: AWS S3 for rendered outputs
- **Deployment**: RunPod (GPU-based inference)

### Infrastructure
- **Containerization**: Docker with multi-stage builds
- **Development**: Docker Compose for local environment
- **Production**: Optimized production Dockerfile
- **Logging**: Structured logging with Loguru

### Security
- **Password Security**: bcrypt with salt rounds
- **Token Security**: JWT with configurable expiration
- **CORS**: Configured middleware for cross-origin requests
- **Environment Variables**: Secure credential management

## Architecture Highlights

### Modular Design
- **Controller-Service Pattern**: Clear separation of concerns
- **Dependency Injection**: AsyncSession and user context management
- **Schema Validation**: Pydantic models for request/response validation
- **Error Handling**: Comprehensive exception handling with proper HTTP status codes

### Performance Optimizations
- **Asynchronous Operations**: Full async/await support for I/O operations
- **Image Compression**: Binary search for optimal JPEG quality
- **GPU Acceleration**: Tensor operations on CUDA when available
- **Background Tasks**: Non-blocking file cleanup and processing
- **Connection Pooling**: Efficient database connection management

### Scalability Features
- **Session-based Processing**: Support for anonymous and authenticated users
- **Batch Operations**: Bulk file operations and commits
- **Horizontal Scaling**: Stateless API design
- **Cloud-Native**: Containerized, deployable to any container platform

## Deployment
- **Containerized Application**: Multi-stage Docker builds for optimization
- **RunPod Integration**: GPU-accelerated inference on cloud infrastructure
- **Environment Configuration**: Comprehensive .env-based configuration
- **Database Migrations**: Automated schema versioning

## Key Metrics & Capabilities
- **Image Processing**: Supports up to 16MP images (4096px max dimension)
- **File Size Optimization**: Automatic compression to meet 9.5MB API limits
- **Processing Speed**: GPU-accelerated inference with async I/O
- **Material Catalog**: Hierarchical organization of 100+ material options
- **Supported Elements**: Walls, Roofs, Windows, Doors, Masonry, Trim, Siding, Garages


