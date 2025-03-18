class TableFormatter:
    @staticmethod
    def format_triple_table(triples):
        """
        Format a list of triples into a displayable table
        
        Args:
            triples: List of triple dictionaries with keys 'T', 'OP', 'OPE1', 'OPE2'
            
        Returns:
            Formatted table as a string
        """
        if not triples:
            return "No triples generated."
        
        # Calculate column widths
        t_width = max(5, max(len(triple['T']) for triple in triples))
        op_width = max(4, max(len(triple['OP']) for triple in triples))
        ope1_width = max(4, max(len(str(triple['OPE1'])) for triple in triples))
        ope2_width = max(4, max(len(str(triple['OPE2'])) for triple in triples))
        
        # Create header
        header = f"| {'T'.ljust(t_width)} | {'OP'.ljust(op_width)} | {'OPE1'.ljust(ope1_width)} | {'OPE2'.ljust(ope2_width)} |"
        separator = f"| {'-' * t_width} | {'-' * op_width} | {'-' * ope1_width} | {'-' * ope2_width} |"
        
        # Create table rows
        rows = [header, separator]
        for triple in triples:
            row = f"| {triple['T'].ljust(t_width)} | {triple['OP'].ljust(op_width)} | {str(triple['OPE1']).ljust(ope1_width)} | {str(triple['OPE2']).ljust(ope2_width)} |"
            rows.append(row)
        
        return '\n'.join(rows) 