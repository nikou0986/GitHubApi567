
import  unittest
from homework_api import get_api
from unittest import mock



class TestMockApi(unittest.TestCase):   
    def test_mock_api(self):
        r=get_api()
        r.get_info_api = mock.Mock(return_value = "The user has 2 repos, names and commits as follows: /nName: GitHubApi567; Commits: 9 /nName: Triangle567; Commits: 9")
        result = r.get_info_api("yalilu")
        self.assertEqual(result, "The user has 2 repos, names and commits as follows: /nName: GitHubApi567; Commits: 9 /nName: Triangle567; Commits: 9")
        
    
if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
   

