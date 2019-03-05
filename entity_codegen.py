"""
An example how to generate angularjs code from textX model using jinja2
template engine (http://jinja.pocoo.org/docs/dev/)
"""
from os import mkdir
from os.path import exists, dirname, join
import jinja2
from entity_test import get_entity_mm


def main(debug=False):

    this_folder = dirname(__file__)

    entity_mm = get_entity_mm(debug)

    # Build Person model from person.ent file
    person_model = entity_mm.model_from_file(join(this_folder, 'person.ent'))
    ejemplo_model = entity_mm.model_from_file(join(this_folder, 'ejemplo.ent'))
    conexion_model = entity_mm.model_from_file(join(this_folder, 'conexion.ent'))
    
    
    
    def is_entity(n):
        """
        Test to prove if some type is an entity
        """
        if n.type in person_model.entities:
            return True
        else:
            return False

    def rubytype(s):
        """
        Maps type names from PrimitiveType to Java.
        """
        return {
                'integer': 'int',
                'string': 'String'
        }.get(s.name, s.name)
    
    def sqltype(s):
        """
        Maps type names from PrimitiveType to Java.
        """
        return {
                'integer': 'int',
                'varchar': 'varchar (255)'
        }.get(s.name, s.name)
    
    # Create output folder
    srcgen_folder = join(this_folder, 'srcgen')
    if not exists(srcgen_folder):
        mkdir(srcgen_folder)

    # Initialize template engine.
    jinja_env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(this_folder),
        trim_blocks=True,
        lstrip_blocks=True)

    # Register filter for mapping Entity type names to Java type names.

    jinja_env.tests['entity'] = is_entity
    jinja_env.filters['rubytype'] = rubytype
    jinja_env.filters['sqltype'] = sqltype

    # Load template
    template = jinja_env.get_template('clase.template')
    
    for entity in person_model.entities:
    # For each entity generate ruby file
        with open(join(srcgen_folder,
                        "%s.rb" % entity.name.capitalize()), 'w') as f:
            f.write(template.render(entity=entity))

    template = jinja_env.get_template('conexionClass.template')
    
    for entity in conexion_model.entities:
    # For each entity generate sql file
        with open(join(srcgen_folder,
                       "%s.rb" % entity.name.capitalize()), 'w') as f:
            f.write(template.render(entity=entity))
    
    template = jinja_env.get_template('base.template')
    
    for entity in ejemplo_model.entities:
    # For each entity generate sql file
        with open(join(srcgen_folder,
                       "%s.sql" % "Script"), 'w') as f:
            f.write(template.render(entity=entity))
    
    template = jinja_env.get_template('tabla.template')
    
    for entity in ejemplo_model.entities:
        # For each entity generate sql file
        with open(join(srcgen_folder,
                       "%s.sql" % "Script"), 'a') as f:
            f.write(template.render(entity=entity))

    template = jinja_env.get_template('llaves.template')
    
    for entity in ejemplo_model.entities:
        # For each entity generate sql file
        with open(join(srcgen_folder,
                       "%s.sql" % "Script"), 'a') as f:
            f.write(template.render(entity=entity))
    
    
if __name__ == "__main__":
    main()
