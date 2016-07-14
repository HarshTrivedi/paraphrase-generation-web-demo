from nltk import word_tokenize
from nltk.tree import MultiParentedTree
from awesome_print import ap
from bllipparser import RerankingParser
from bllipparser.ModelFetcher import download_and_install_model
import itertools



parsed_string = "(S1 (S (NP (DT The) (NN fighting)) (NP (JJ last) (NN week)) (VP (VBD killed) (NP (QP (IN at) (JJS least) (CD 12))))))"

ptree = MultiParentedTree.fromstring( parsed_string  )

for check_node in ptree.subtrees():
	if len(list(check_node)) > 2: 
		if check_node[0].label() == check_node[1].label():
			check_node[0].extend(check_node[1])
			check_node.remove(check_node[1])
		elif check_node[1].label() == check_node[2].label():
			check_node[1].extend(check_node[2])
			check_node.remove(check_node[2])

ptree.draw()
# ptree1[0][0].extend(ptree1[0][1])
# ptree1[0].remove(ptree1[0][1])