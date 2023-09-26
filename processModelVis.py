from pm4py.objects.log.importer.csv import factory as csv_importer
from pm4py.objects.conversion.log import factory as conversion_factory
from pm4py.objects.log.adapters.pandas import csv_import_adapter
from pm4py.util import constants
from pm4py.algo.discovery.inductive import factory as inductive_miner
from pm4py.algo.discovery.dfg import factory as dfg_factory
from pm4py.visualization.petrinet import factory as pt_vis_factory
from pm4py.algo.conformance.alignments import factory as align_factory
from pm4py.evaluation.replay_fitness import factory as replay_fitness_factory
import config
from pm4py.visualization.heuristics_net import factory as hn_vis_factory
from pm4py.visualization.dfg import factory as dfg_vis_factory
from pm4py.algo.discovery.heuristics import factory as heuristics_miner


def inductiveMinerProcessModelVis(dataframe):
    log = conversion_factory.apply(dataframe)

    net, initial_marking, final_marking = inductive_miner.apply(log)
    gviz = pt_vis_factory.apply(net, initial_marking, final_marking, parameters={"format": "svg"})
    # alignments = align_factory.apply_log(log, net, initial_marking, final_marking)
    # print(alignments)
    pt_vis_factory.save(gviz, config.processModelVis+".svg")

    # log_fitness = replay_fitness_factory.evaluate(alignments, variant="alignments")
    # print(">>>>>Log_fitness: ")
    # print(log_fitness)

def heuristicMinerProcessModelVis(dataframe):
    log = conversion_factory.apply(dataframe)
    heu_net = heuristics_miner.apply_heu(log, parameters={"dependency_thresh": 0.99,"format": "png"})
    gviz = hn_vis_factory.apply(heu_net)
    hn_vis_factory.save(gviz, config.processModelVis+".png")

def dfgProcessModelVis(dataframe):
    log = conversion_factory.apply(dataframe)
    dfg = dfg_factory.apply(log, variant="frequency")
    parameters = {"format": "svg"}
    gviz = dfg_vis_factory.apply(dfg, log=log, variant="frequency", parameters=parameters)
    dfg_vis_factory.save(gviz, config.processModelVis+"dfg.svg")

