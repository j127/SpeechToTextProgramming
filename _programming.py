"""
    This module is a simple example of Dragonfly use.

    It shows how to use Dragonfly's Grammar, AppContext, and MappingRule
    classes.  This module can be activated in the same way as other
    Natlink macros by placing it in the "My Documents\Natlink folder" or
    "Program Files\NetLink/MacroSystem".

"""

from dragonfly import (Grammar, AppContext, MappingRule, Dictation,
                       Key, Text)


#---------------------------------------------------------------------------
# Create this module's grammar and the context under which it'll be active.

programming_context = AppContext(executable="subl.exe")
grammar = Grammar("sublime_text", context=programming_context)


#---------------------------------------------------------------------------
# Create a mapping rule which maps things you can say to actions.
#
# Note the relationship between the *mapping* and *extras* keyword
#  arguments.  The extras is a list of Dragonfly elements which are
#  available to be used in the specs of the mapping.  In this example
#  the Dictation("text")* extra makes it possible to use "<text>"
#  within a mapping spec and "%(text)s" within the associated action.

programming_rule = MappingRule(
    name="escape",    # The name of the rule.
    mapping={          # The mapping dict: spec -> action.
             "escape":            Key("esc")
            },
    extras=[           # Special elements in the specs of the mapping.
            #Dictation("text"),
           ],
    )

# Add the action rule to the grammar instance.
grammar.add_rule(programming_rule)


#---------------------------------------------------------------------------
# Load the grammar instance and define how to unload it.

grammar.load()

# Unload function which will be called by natlink at unload time.
def unload():
    global grammar
    if grammar: grammar.unload()
    grammar = None
