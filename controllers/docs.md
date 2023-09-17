## Get All Materials

**URL:**

`GET /api/materials`

**Response** (list format):

```json
[
    {
        "id": 47,
        "code": "JNS001",
        "name": "Raw Denim",
        "type": "jeans",
        "buy_price": 150.0,
        "supplier_id": [
            11,
            "Denim World Ltd."
        ]
    },
    {
        "id": 49,
        "code": "CTN001",
        "name": "Organic Cotton",
        "type": "cotton",
        "buy_price": 130.0,
        "supplier_id": [
            10,
            "TexFab Inc."
        ]
    }
]
```

## Create Material

**URL:**  
`POST /api/materials`

**Request Body** (in dictionary format):

```json
{
    "params": {
        "code": "<MATERIAL_CODE>",
        "name": "<MATERIAL_NAME>",
        "type": "<MATERIAL_TYPE>",
        "buy_price": "<BUY_PRICE>",
        "supplier_id": "<SUPPLIER_ID>"
    }
}

**Response:**

```json
{
    "jsonrpc": "2.0",
    "id": null,
    "result": {
        "code": 200,
        "message": "Material created successfully with ID: 66!"
    }
}
```

## Update Material

**URL:**  
`PUT /api/materials/<MATERIAL_ID>`

**Request Body** (fields to be updated):

```json
{
    "params": {
        "code": "<MATERIAL_CODE>",
        "name": "<MATERIAL_NAME>",
        "type": "<MATERIAL_TYPE>",
        "buy_price": "<BUY_PRICE>",
        "supplier_id": "<SUPPLIER_ID>"
    }
}

**Responses:**

- **Successful update:**

```json
{
    "jsonrpc": "2.0",
    "id": null,
    "result": {
        "code": 200,
        "message": "Material updated successfully!"
    }
}
```

## Delete Material

**URL:** 
`DELETE /api/materials/<MATERIAL_ID>`

**Responses:**

```json
{
    "code": 200,
    "message": "Material deleted successfully!"
}
```
