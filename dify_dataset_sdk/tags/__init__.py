"""Tags and metadata module for Dify Dataset SDK."""

from .client import TagsClient
from .models import (
    BindDatasetToTagRequest,
    CreateKnowledgeTagRequest,
    CreateMetadataRequest,
    DeleteKnowledgeTagRequest,
    DocumentMetadata,
    KnowledgeTag,
    Metadata,
    MetadataListResponse,
    MetadataValue,
    UnbindDatasetFromTagRequest,
    UpdateDocumentMetadataRequest,
    UpdateKnowledgeTagRequest,
    UpdateMetadataRequest,
)

__all__ = [
    "TagsClient",
    "KnowledgeTag",
    "CreateKnowledgeTagRequest",
    "UpdateKnowledgeTagRequest",
    "DeleteKnowledgeTagRequest",
    "BindDatasetToTagRequest",
    "UnbindDatasetFromTagRequest",
    "Metadata",
    "MetadataValue",
    "DocumentMetadata",
    "MetadataListResponse",
    "CreateMetadataRequest",
    "UpdateMetadataRequest",
    "UpdateDocumentMetadataRequest",
]
