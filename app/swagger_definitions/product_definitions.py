product_list_definition = {
    "summary": "Retrieve all products",
    "description": "Fetches a list of all products available in the store.",
    "responses": {
        200: {
            "description": "A list of products",
            "content": {
                "application/json": {
                    "example": [
                        {
                            "id": 1,
                            "name": "Waffle with Berries",
                            "category": "Waffle",
                            "price": 6.50,
                            "image_thumbnail": "./assets/images/image-waffle-thumbnail.jpg",
                            "image_mobile": "./assets/images/image-waffle-mobile.jpg",
                            "image_tablet": "./assets/images/image-waffle-tablet.jpg",
                            "image_desktop": "./assets/images/image-waffle-desktop.jpg"
                        }
                    ]
                }
            }
        }
    }
}

product_detail_definition = {
    "summary": "Retrieve a specific product",
    "description": "Fetches details of a product by its ID.",
    "parameters": [
        {
            "name": "id",
            "in": "path",
            "required": True,
            "description": "The ID of the product to retrieve.",
            "schema": {"type": "integer"}
        }
    ],
    "responses": {
        200: {
            "description": "Product details",
            "content": {
                "application/json": {
                    "example": {
                        "id": 1,
                        "name": "Waffle with Berries",
                        "category": "Waffle",
                        "price": 6.50,
                        "image_thumbnail": "./assets/images/image-waffle-thumbnail.jpg",
                        "image_mobile": "./assets/images/image-waffle-mobile.jpg",
                        "image_tablet": "./assets/images/image-waffle-tablet.jpg",
                        "image_desktop": "./assets/images/image-waffle-desktop.jpg"
                    }
                }
            }
        },
        404: {
            "description": "Product not found"
        }
    }
}

product_create_definition = {
    "summary": "Add a new product",
    "description": "Creates a new product in the store (admin functionality).",
    "requestBody": {
        "required": True,
        "content": {
            "application/json": {
                "schema": {
                    "type": "object",
                    "properties": {
                        "name": {"type": "string"},
                        "category": {"type": "string"},
                        "price": {"type": "number"},
                        "image_thumbnail": {"type": "string"},
                        "image_mobile": {"type": "string"},
                        "image_tablet": {"type": "string"},
                        "image_desktop": {"type": "string"}
                    },
                    "required": ["name", "category", "price", "image_thumbnail", "image_mobile", "image_tablet", "image_desktop"]
                },
                "example": {
                    "name": "Chocolate Cake",
                    "category": "Dessert",
                    "price": 10.50,
                    "image_thumbnail": "path/to/thumbnail.jpg",
                    "image_mobile": "path/to/mobile.jpg",
                    "image_tablet": "path/to/tablet.jpg",
                    "image_desktop": "path/to/desktop.jpg"
                }
            }
        }
    },
    "responses": {
        201: {
            "description": "Product created successfully",
            "content": {
                "application/json": {
                    "example": {
                        "id": 4,
                        "name": "Chocolate Cake",
                        "category": "Dessert",
                        "price": 10.50,
                        "image_thumbnail": "path/to/thumbnail.jpg",
                        "image_mobile": "path/to/mobile.jpg",
                        "image_tablet": "path/to/tablet.jpg",
                        "image_desktop": "path/to/desktop.jpg"
                    }
                }
            }
        },
        403: {
            "description": "Unauthorized access"
        }
    }
}

product_update_definition = {
    "summary": "Update an existing product",
    "description": "Updates details of an existing product (admin functionality).",
    "parameters": [
        {
            "name": "id",
            "in": "path",
            "required": True,
            "description": "The ID of the product to update.",
            "schema": {"type": "integer"}
        }
    ],
    "requestBody": {
        "required": True,
        "content": {
            "application/json": {
                "schema": {
                    "type": "object",
                    "properties": {
                        "name": {"type": "string"},
                        "category": {"type": "string"},
                        "price": {"type": "number"},
                        "image_thumbnail": {"type": "string"},
                        "image_mobile": {"type": "string"},
                        "image_tablet": {"type": "string"},
                        "image_desktop": {"type": "string"}
                    }
                },
                "example": {
                    "name": "Updated Cake",
                    "category": "Dessert",
                    "price": 12.00,
                    "image_thumbnail": "updated/path/to/thumbnail.jpg",
                    "image_mobile": "updated/path/to/mobile.jpg",
                    "image_tablet": "updated/path/to/tablet.jpg",
                    "image_desktop": "updated/path/to/desktop.jpg"
                }
            }
        }
    },
    "responses": {
        200: {
            "description": "Product updated successfully",
            "content": {
                "application/json": {
                    "example": {
                        "id": 4,
                        "name": "Updated Cake",
                        "category": "Dessert",
                        "price": 12.00,
                        "image_thumbnail": "updated/path/to/thumbnail.jpg",
                        "image_mobile": "updated/path/to/mobile.jpg",
                        "image_tablet": "updated/path/to/tablet.jpg",
                        "image_desktop": "updated/path/to/desktop.jpg"
                    }
                }
            }
        },
        404: {
            "description": "Product not found"
        }
    }
}

product_delete_definition = {
    "summary": "Delete a product",
    "description": "Deletes a product by its ID (admin functionality).",
    "parameters": [
        {
            "name": "id",
            "in": "path",
            "required": True,
            "description": "The ID of the product to delete.",
            "schema": {"type": "integer"}
        }
    ],
    "responses": {
        200: {
            "description": "Product deleted successfully",
            "content": {
                "application/json": {
                    "example": {
                        "message": "Product deleted successfully"
                    }
                }
            }
        },
        404: {
            "description": "Product not found"
        }
    }
}
