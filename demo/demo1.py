from slimit.parser import Parser
from slimit.visitors import nodevisitor
from slimit import ast


class JavaScriptIfEvaluator:
    def __init__(self, formula):
        self.formula = formula

    def evaluate(self, context=None):
        try:
            parser = Parser()
            tree = parser.parse(self.formula)

            for node in nodevisitor.visit(tree):
                if isinstance(node, ast.Identifier):
                    # Check for identifiers and replace them with values from the context if available
                    if context and node.value in context:
                        node.replace_with(ast.Literal(context[node.value]))

            # Evaluate the modified tree
            modified_formula = tree.to_ecma()
            result = eval(modified_formula, {})

            return result

        except Exception as e:
            return f"Error: {str(e)}"


# Example usage:
if_formula = 'if (a > 10) { "High" } else { "Low" }'
context = {"a": 15}

if_evaluator = JavaScriptIfEvaluator(if_formula)
result = if_evaluator.evaluate(context)
print(f"Result: {result}")
