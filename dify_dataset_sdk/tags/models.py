"""Models for tags and metadata module."""

from typing import List, Optional

from pydantic import BaseModel, ConfigDict, Field


# ===== Knowledge Tag Models =====
class KnowledgeTag(BaseModel):
    """Knowledge base tag information."""

    model_config = ConfigDict(extra="ignore")

    id: str = Field(description="Tag ID")
    name: str = Field(description="Tag name")
    color: Optional[str] = Field(None, description="Tag color")
    created_at: Optional[int] = Field(None, description="Creation timestamp")
    updated_at: Optional[int] = Field(None, description="Update timestamp")
    binding_count: Optional[int] = Field(None, description="Number of bindings")


class CreateKnowledgeTagRequest(BaseModel):
    """Request model for creating knowledge tag."""

    model_config = ConfigDict(extra="ignore")

    name: str = Field(description="Tag name", max_length=50)


class UpdateKnowledgeTagRequest(BaseModel):
    """Request model for updating knowledge tag."""

    model_config = ConfigDict(extra="ignore")

    name: str = Field(description="Tag name", max_length=50)
    tag_id: str = Field(description="Tag ID")


class DeleteKnowledgeTagRequest(BaseModel):
    """Request model for deleting knowledge tag."""

    model_config = ConfigDict(extra="ignore")

    tag_id: str = Field(description="Tag ID")


class BindDatasetToTagRequest(BaseModel):
    """Request model for binding dataset to knowledge tag."""

    model_config = ConfigDict(extra="ignore")

    tag_ids: List[str] = Field(description="Tag ID list")
    target_id: str = Field(description="Dataset ID")


class UnbindDatasetFromTagRequest(BaseModel):
    """Request model for unbinding dataset from knowledge tag."""

    model_config = ConfigDict(extra="ignore")

    tag_id: str = Field(description="Tag ID")
    target_id: str = Field(description="Dataset ID")


# ===== Metadata Models =====
class Metadata(BaseModel):
    """Metadata field information."""

    model_config = ConfigDict(extra="ignore")

    id: str = Field(description="Metadata field ID")
    type: str = Field(description="Field type")
    name: str = Field(description="Field name")
    use_count: Optional[int] = Field(None, description="Usage count")


class MetadataValue(BaseModel):
    """Metadata value information."""

    model_config = ConfigDict(extra="ignore")

    id: str = Field(description="Metadata field ID")
    value: str = Field(description="Metadata value")
    name: str = Field(description="Field name")


class DocumentMetadata(BaseModel):
    """Document metadata association."""

    model_config = ConfigDict(extra="ignore")

    document_id: str = Field(description="Document ID")
    metadata_list: List[MetadataValue] = Field(description="Metadata values")


class CreateMetadataRequest(BaseModel):
    """Request model for creating metadata field."""

    model_config = ConfigDict(extra="ignore")

    type: str = Field(description="Metadata type")
    name: str = Field(description="Metadata name")


class UpdateMetadataRequest(BaseModel):
    """Request model for updating metadata field."""

    model_config = ConfigDict(extra="ignore")

    name: str = Field(description="Metadata name")


class UpdateDocumentMetadataRequest(BaseModel):
    """Request model for updating document metadata."""

    model_config = ConfigDict(extra="ignore")

    operation_data: List[DocumentMetadata] = Field(description="Document metadata operations")


class MetadataListResponse(BaseModel):
    """Response model for metadata list."""

    model_config = ConfigDict(extra="ignore")

    doc_metadata: List[Metadata] = Field(description="Metadata fields")
    built_in_field_enabled: bool = Field(description="Built-in field enabled status")
