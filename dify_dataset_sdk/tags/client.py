"""Tags and metadata client for Dify API."""

from typing import Any, Dict, List, Literal, Union

from .._base import BaseClient
from .models import (
    BindDatasetToTagRequest,
    CreateKnowledgeTagRequest,
    CreateMetadataRequest,
    DeleteKnowledgeTagRequest,
    DocumentMetadata,
    KnowledgeTag,
    Metadata,
    MetadataListResponse,
    UnbindDatasetFromTagRequest,
    UpdateDocumentMetadataRequest,
    UpdateKnowledgeTagRequest,
    UpdateMetadataRequest,
)


class TagsClient:
    """Client for tag and metadata management operations.

    Provides methods for managing knowledge tags and metadata fields.
    """

    def __init__(self, base_client: BaseClient) -> None:
        """Initialize the tags client.

        Args:
            base_client: Base HTTP client for making API requests
        """
        self._client = base_client

    # ===== Knowledge Tag Operations =====
    def create(self, name: str) -> KnowledgeTag:
        """Create a new knowledge type tag.

        Args:
            name: Tag name (max 50 characters)

        Returns:
            Created tag information

        Raises:
            DifyValidationError: If name is invalid or too long
            DifyAPIError: For other API errors
        """
        request = CreateKnowledgeTagRequest(name=name)
        response = self._client.post("/v1/datasets/tags", json=request.model_dump())
        return KnowledgeTag(**response)

    def list(self) -> List[KnowledgeTag]:
        """Get list of knowledge type tags.

        Returns:
            List of knowledge tags

        Raises:
            DifyAPIError: For API errors
        """
        response = self._client.get("/v1/datasets/tags")
        # Handle both list and dict response formats
        if isinstance(response, list):
            return [KnowledgeTag(**tag) for tag in response]
        else:
            return [KnowledgeTag(**tag) for tag in response.get("data", [])]

    def update(self, tag_id: str, name: str) -> KnowledgeTag:
        """Update knowledge type tag name.

        Args:
            tag_id: Tag ID
            name: New tag name (max 50 characters)

        Returns:
            Updated tag information

        Raises:
            DifyNotFoundError: If tag not found
            DifyValidationError: If name is invalid
            DifyAPIError: For other API errors
        """
        request = UpdateKnowledgeTagRequest(name=name, tag_id=tag_id)
        response = self._client.patch("/v1/datasets/tags", json=request.model_dump())
        return KnowledgeTag(**response)

    def delete(self, tag_id: str) -> Dict[str, Any]:
        """Delete a knowledge type tag.

        Args:
            tag_id: Tag ID

        Returns:
            Success response

        Raises:
            DifyNotFoundError: If tag not found
            DifyAPIError: For other API errors
        """
        request = DeleteKnowledgeTagRequest(tag_id=tag_id)
        return self._client.delete("/v1/datasets/tags", json=request.model_dump())

    def bind_to_dataset(
        self,
        dataset_id: str,
        tag_ids: List[str],
    ) -> Dict[str, Any]:
        """Bind dataset to knowledge type tags.

        Args:
            dataset_id: Dataset ID
            tag_ids: List of tag IDs

        Returns:
            Success response

        Raises:
            DifyNotFoundError: If dataset or tags not found
            DifyValidationError: If tag IDs are invalid
            DifyAPIError: For other API errors
        """
        request = BindDatasetToTagRequest(tag_ids=tag_ids, target_id=dataset_id)
        return self._client.post("/v1/datasets/tags/binding", json=request.model_dump())

    def unbind_from_dataset(
        self,
        dataset_id: str,
        tag_id: str,
    ) -> Dict[str, Any]:
        """Unbind dataset from knowledge type tag.

        Args:
            dataset_id: Dataset ID
            tag_id: Tag ID

        Returns:
            Success response

        Raises:
            DifyNotFoundError: If dataset or tag not found
            DifyAPIError: For other API errors
        """
        request = UnbindDatasetFromTagRequest(tag_id=tag_id, target_id=dataset_id)
        return self._client.post("/v1/datasets/tags/unbinding", json=request.model_dump())

    def get_dataset_tags(self, dataset_id: str) -> List[KnowledgeTag]:
        """Get tags bound to a dataset.

        Args:
            dataset_id: Dataset ID

        Returns:
            List of bound tags

        Raises:
            DifyNotFoundError: If dataset not found
            DifyAPIError: For other API errors
        """
        response = self._client.get(f"/v1/datasets/{dataset_id}/tags")
        # Handle both list and dict response formats
        if isinstance(response, list):
            return [KnowledgeTag(**tag) for tag in response]
        else:
            return [KnowledgeTag(**tag) for tag in response.get("data", [])]

    # ===== Metadata Operations =====
    def create_metadata(
        self,
        dataset_id: str,
        field_type: str,
        name: str,
    ) -> Metadata:
        """Create a metadata field for a dataset.

        Args:
            dataset_id: Dataset ID
            field_type: Metadata type (string, number, time)
            name: Field name

        Returns:
            Created metadata field information

        Raises:
            DifyNotFoundError: If dataset not found
            DifyValidationError: If field data is invalid
            DifyAPIError: For other API errors
        """
        request = CreateMetadataRequest(type=field_type, name=name)
        response = self._client.post(f"/v1/datasets/{dataset_id}/metadata", json=request.model_dump())
        return Metadata(**response)

    def update_metadata(
        self,
        dataset_id: str,
        metadata_id: str,
        name: str,
    ) -> Metadata:
        """Update a metadata field.

        Args:
            dataset_id: Dataset ID
            metadata_id: Metadata field ID
            name: Updated field name

        Returns:
            Updated metadata field information

        Raises:
            DifyNotFoundError: If dataset or metadata field not found
            DifyValidationError: If field data is invalid
            DifyAPIError: For other API errors
        """
        request = UpdateMetadataRequest(name=name)
        response = self._client.patch(
            f"/v1/datasets/{dataset_id}/metadata/{metadata_id}",
            json=request.model_dump(),
        )
        return Metadata(**response)

    def delete_metadata(
        self,
        dataset_id: str,
        metadata_id: str,
    ) -> Dict[str, Any]:
        """Delete a metadata field.

        Args:
            dataset_id: Dataset ID
            metadata_id: Metadata field ID

        Returns:
            Success response

        Raises:
            DifyNotFoundError: If dataset or metadata field not found
            DifyAPIError: For other API errors
        """
        return self._client.delete(f"/v1/datasets/{dataset_id}/metadata/{metadata_id}")

    def toggle_built_in_metadata(
        self,
        dataset_id: str,
        action: Literal["disable", "enable"],
    ) -> Dict[str, Any]:
        """Enable or disable built-in metadata fields.

        Args:
            dataset_id: Dataset ID
            action: Action to perform - 'disable' or 'enable'

        Returns:
            Success response

        Raises:
            DifyNotFoundError: If dataset not found
            DifyValidationError: If action is invalid
            DifyAPIError: For other API errors
        """
        return self._client.post(f"/v1/datasets/{dataset_id}/metadata/built-in/{action}")

    def update_document_metadata(
        self,
        dataset_id: str,
        operation_data: Union[List[DocumentMetadata], List[Dict[str, Any]]],
    ) -> Dict[str, Any]:
        """Update document metadata values.

        Args:
            dataset_id: Dataset ID
            operation_data: List of document metadata operations, each containing:
                - document_id (str): Document ID
                - metadata_list (list): Metadata list with id, value, name

        Returns:
            Success response

        Raises:
            DifyNotFoundError: If dataset not found
            DifyValidationError: If metadata is invalid
            DifyAPIError: For other API errors
        """
        # Convert dicts to DocumentMetadata if needed
        converted_data: List[DocumentMetadata] = []
        for item in operation_data:
            if isinstance(item, dict):
                converted_data.append(DocumentMetadata(**item))
            else:
                converted_data.append(item)
        request = UpdateDocumentMetadataRequest(operation_data=converted_data)
        result: Dict[str, Any] = self._client.post(f"/v1/datasets/{dataset_id}/documents/metadata", json=request.model_dump())
        return result

    def list_metadata(self, dataset_id: str) -> MetadataListResponse:
        """Get list of metadata fields for a dataset.

        Args:
            dataset_id: Dataset ID

        Returns:
            List of metadata fields

        Raises:
            DifyNotFoundError: If dataset not found
            DifyAPIError: For other API errors
        """
        response = self._client.get(f"/v1/datasets/{dataset_id}/metadata")
        return MetadataListResponse(**response)
