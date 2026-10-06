e=$1
python3 render_parts.py $e 0 45 && python3 render_parts.py $e 45 90 && python3 render_parts.py $e 90 300 && python3 render_parts.py $e mux
