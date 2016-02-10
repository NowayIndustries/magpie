from __future__ import division, unicode_literals

import unittest

from magpie.evaluation.standard_evaluation import evaluate_results


class TestEvaluateResults(unittest.TestCase):
    def test_evaluate_results1(self):
        kw_mask = [0.5, 0.3, 0.8, 0.6]
        kw_vector = [
            (1, "supersymmetry"),
            (2, "numerical calculations"),
            (2, "quantum chromodynamics"),
            (3, "bibliography"),
        ]
        gt_answers = {
            1: {"supersymmetry", "string model"},
            2: {"numerical calculations"},
            3: {"duality", "membrane model"},
            4: {"lattice field theory"},
        }

        metrics = evaluate_results(
            kw_mask,
            kw_vector,
            gt_answers
        )

        self.assertAlmostEqual(metrics['p_at_3'], 0.25)
        self.assertAlmostEqual(metrics['p_at_5'], 0.15)
        self.assertAlmostEqual(metrics['mrr'], 215 / 456)
        self.assertAlmostEqual(metrics['map'], 1561 / 4560)
        self.assertAlmostEqual(metrics['r_prec'], 81 / 380)

    def test_evaluate_results2(self):
        kw_mask = [0.8, 0.7, 0.3, 0.5, 0.1, 0.6, 0.9]
        kw_vector = [
            (1, "supersymmetry"),
            (1, "experimental results"),
            (2, "numerical calculations"),
            (2, "quantum chromodynamics"),
            (3, "bibliography"),
            (4, "boundary condition"),
            (4, "critical phenomena"),
        ]
        gt_answers = {
            1: {"supersymmetry", "string model", "experimental results", "cosmological model"},
            2: {"numerical calculations", "quantum chromodynamics"},
            3: {"duality", "membrane model"},
            4: {"critical phenomena"},
            5: {"lattice field theory", "CERN LHC Coll"},
        }

        metrics = evaluate_results(
            kw_mask,
            kw_vector,
            gt_answers
        )

        self.assertAlmostEqual(metrics['p_at_3'], 7 / 15)
        self.assertAlmostEqual(metrics['p_at_5'], 8 / 25)
        self.assertAlmostEqual(metrics['mrr'], 43 / 60)
        self.assertAlmostEqual(metrics['map'], 7397 / 11400)
        self.assertAlmostEqual(metrics['r_prec'], 733 / 1425)
