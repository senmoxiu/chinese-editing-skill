"""Check that the repository validator rejects broken distributable packages."""
import importlib.util
from pathlib import Path
import shutil
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("validate", ROOT / "scripts" / "validate.py")
validator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validator)


class PackageValidationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="chinese-editing-test-")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / "package"
        shutil.copytree(ROOT, self.root, ignore=shutil.ignore_patterns(".git", "__pycache__", ".venv"))

    def test_distributable_is_valid(self):
        self.assertEqual([], validator.validate(self.root)[0])

    def test_missing_referenced_file_is_rejected(self):
        entry = self.root / "skills/chinese-editing/SKILL.md"
        entry.write_text(entry.read_text(encoding="utf-8") + "\n[Missing](references/missing.md)\n", encoding="utf-8")
        self.assertTrue(any("missing link target" in e for e in validator.validate(self.root)[0]))

    def test_link_outside_package_is_rejected(self):
        outside = Path(self.temp.name) / "outside.md"
        outside.write_text("outside package", encoding="utf-8")
        readme = self.root / "README.md"
        readme.write_text(readme.read_text(encoding="utf-8") + "\n[Outside](../outside.md)\n", encoding="utf-8")
        self.assertTrue(any("escapes repository" in e for e in validator.validate(self.root)[0]))

    def test_wrong_skill_name_is_rejected(self):
        entry = self.root / "skills/chinese-editing/SKILL.md"
        entry.write_text(entry.read_text(encoding="utf-8").replace("name: chinese-editing", "name: something-else", 1), encoding="utf-8")
        self.assertTrue(any("name and directory differ" in e for e in validator.validate(self.root)[0]))


if __name__ == "__main__":
    unittest.main()
