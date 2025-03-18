class FormateadorTabla:
    @staticmethod
    def formatear_tabla_triplos(triplos):
        """
        Formatea una lista de triplos en una tabla mostrable
        
        Args:
            triplos: Lista de diccionarios de triplos con claves 'T', 'OP', 'OPE1', 'OPE2'
            
        Returns:
            Tabla formateada como una cadena de texto
        """
        if not triplos:
            return "No se generaron triplos."
        
        # Calcular anchos de columnas
        ancho_t = max(5, max(len(triplo['T']) for triplo in triplos))
        ancho_op = max(4, max(len(triplo['OP']) for triplo in triplos))
        ancho_ope1 = max(4, max(len(str(triplo['OPE1'])) for triplo in triplos))
        ancho_ope2 = max(4, max(len(str(triplo['OPE2'])) for triplo in triplos))
        
        # Crear encabezado
        encabezado = f"| {'T'.ljust(ancho_t)} | {'OP'.ljust(ancho_op)} | {'OPE1'.ljust(ancho_ope1)} | {'OPE2'.ljust(ancho_ope2)} |"
        separador = f"| {'-' * ancho_t} | {'-' * ancho_op} | {'-' * ancho_ope1} | {'-' * ancho_ope2} |"
        
        # Crear filas de la tabla
        filas = [encabezado, separador]
        for triplo in triplos:
            fila = f"| {triplo['T'].ljust(ancho_t)} | {triplo['OP'].ljust(ancho_op)} | {str(triplo['OPE1']).ljust(ancho_ope1)} | {str(triplo['OPE2']).ljust(ancho_ope2)} |"
            filas.append(fila)
        
        return '\n'.join(filas) 