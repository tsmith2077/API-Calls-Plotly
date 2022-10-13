import unittest
from python_repos_visual import repo_links, stars, labels, repo_dicts, r

class TestPythonRepos(unittest.TestCase):
    """Tests for python_repos.py"""
    
    def test_status_code(self):
        """Is status_code returning 200?"""
        self.assertEqual(r.status_code, 200)
        
    def test_returned_dicts(self):
        """Are 30 dictionaries being returned?"""
        self.assertEqual(len(repo_dicts), 30)
    
    def test_length_repo_links(self):
        """Is the length of repo_links 30?"""
        self.assertEqual(len(repo_links), 30)
        
    def test_length_stars(self):
        """Is the length of stars 30?"""
        self.assertEqual(len(stars), 30)
        
    def test_length_labels(self):
        """Is the length of labels 30?"""
        self.assertEqual(len(labels), 30)
        
    if __name__ == '__main__':
        unittest.main