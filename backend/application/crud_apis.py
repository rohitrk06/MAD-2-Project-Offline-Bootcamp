from flask_restful import Resource
from models import *
from flask import make_response, jsonify, request

class CategoryResource(Resource):
    def get(self, category_id):
        category = Categories.query.get(category_id)
        if not category:
            return {'message': 'Category not found'}, 404
        
        result = {
            'message': 'Category retrieved successfully',
            'category': {
                'id': category.id,
                'name': category.name,
                'description': category.description
            }
        }

        return make_response(jsonify(result), 200)
    
    def post(self):
        category_data = request.get_json()
        if not category_data or 'name' not in category_data:
            return {'message': 'Category name is required'}, 400
        
        new_category = Categories(
            name=category_data['name'],
            description=category_data.get('description', '')
        )

        # Check if category with the same name already exists
        existing_category = Categories.query.filter_by(name=new_category.name).first()
        if existing_category:
            return {'message': 'Category with this name already exists'}, 400
        
        # Add the new category to the database        
        db.session.add(new_category)
        db.session.commit()
        
        result = {
            'message': 'Category created successfully',
            'category': {
                'id': new_category.id,
                'name': new_category.name,
                'description': new_category.description
            }
        }

        return make_response(jsonify(result), 201)

    def put(self, category_id):
        category_data = request.get_json()
        if not category_data or 'name' not in category_data:
            return {'message': 'Category name is required'}, 400
        
        category = Categories.query.get(category_id)
        if not category:
            return {'message': 'Category not found'}, 404
        
        # Update the category details
        category.name = category_data['name']
        category.description = category_data.get('description', category.description)
        
        db.session.commit()
        
        result = {
            'message': 'Category updated successfully',
            'category': {
                'id': category.id,
                'name': category.name,
                'description': category.description
            }
        }

        return make_response(jsonify(result), 200)