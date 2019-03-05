class Conexion {
	db_config = {
				host = host
				adapter = adapter
				enconding = enconding
				database = database
				schema_search_path = schema_search_path
		
	db_config = db_config.merge({username: '  ', password: '  '})
	require 'pg'
	require 'active_record'
	
	ActiveRecord::Base.establish_connection(db_config)
	
	db_config[:database] = 'Script'
	ActiveRecord::Base.connection.create_database(db_config[:database])
}
end



