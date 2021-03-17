
LAMBDA_EVENT_PR_CREATED = {'resource': '/github-webhook', 'path': '/github-webhook', 'httpMethod': 'POST', 'headers': {'Accept': '*/*', 'CloudFront-Forwarded-Proto': 'https', 'CloudFront-Is-Desktop-Viewer': 'true', 'CloudFront-Is-Mobile-Viewer': 'false', 'CloudFront-Is-SmartTV-Viewer': 'false', 'CloudFront-Is-Tablet-Viewer': 'false', 'CloudFront-Viewer-Country': 'US', 'content-type': 'application/json', 'Host': 'cuicdh0967.execute-api.eu-west-1.amazonaws.com', 'User-Agent': 'GitHub-Hookshot/0cec5b5', 'Via': '1.1 0173aeb09060ae0dd8c77e399d9e5634.cloudfront.net (CloudFront)', 'X-Amz-Cf-Id': 'b7gOV_IqMNaZsgNKsJlUyMeHxoICoIZhfJ29mkbrkgG7eUjVbktjUQ==', 'X-Amzn-Trace-Id': 'Root=1-6051c672-3146c85f3f02e5f43020b351', 'X-Forwarded-For': '', 'X-Forwarded-Port': '443', 'X-Forwarded-Proto': 'https', 'X-GitHub-Delivery': 'd43c34b0-86ff-11eb-84d3-f7961e6da1f1', 'X-GitHub-Event': 'pull_request', 'X-GitHub-Hook-ID': '287104940', 'X-GitHub-Hook-Installation-Target-ID': '29927048', 'X-GitHub-Hook-Installation-Target-Type': 'organization', 'X-Hub-Signature': 'sha1=3b1cbfe48f0966ce55e444182119374eab37e0e4', 'X-Hub-Signature-256': 'sha256=a0af7668eb080ce9ca48e5f545ee8489d1523e488c0079d020b1bd8ed3265e95'}, 'multiValueHeaders': {'Accept': ['*/*'], 'CloudFront-Forwarded-Proto': ['https'], 'CloudFront-Is-Desktop-Viewer': ['true'], 'CloudFront-Is-Mobile-Viewer': ['false'], 'CloudFront-Is-SmartTV-Viewer': ['false'], 'CloudFront-Is-Tablet-Viewer': ['false'], 'CloudFront-Viewer-Country': ['US'], 'content-type': ['application/json'], 'Host': ['cuicdh0967.execute-api.eu-west-1.amazonaws.com'], 'User-Agent': ['GitHub-Hookshot/0cec5b5'], 'Via': ['1.1 0173aeb09060ae0dd8c77e399d9e5634.cloudfront.net (CloudFront)'], 'X-Amz-Cf-Id': ['b7gOV_IqMNaZsgNKsJlUyMeHxoICoIZhfJ29mkbrkgG7eUjVbktjUQ=='], 'X-Amzn-Trace-Id': ['Root=1-6051c672-3146c85f3f02e5f43020b351'], 'X-Forwarded-For': [], 'X-Forwarded-Port': ['443'], 'X-Forwarded-Proto': ['https'], 'X-GitHub-Delivery': ['d43c34b0-86ff-11eb-84d3-f7961e6da1f1'], 'X-GitHub-Event': ['pull_request'], 'X-GitHub-Hook-ID': ['287104940'], 'X-GitHub-Hook-Installation-Target-ID': ['29927048'], 'X-GitHub-Hook-Installation-Target-Type': ['organization'], 'X-Hub-Signature': ['sha1=3b1cbfe48f0966ce55e444182119374eab37e0e4'], 'X-Hub-Signature-256': ['sha256=a0af7668eb080ce9ca48e5f545ee8489d1523e488c0079d020b1bd8ed3265e95']}, 'queryStringParameters': None, 'multiValueQueryStringParameters': None, 'pathParameters': None, 'stageVariables': None, 'requestContext': {'resourceId': 'pq6xlw', 'resourcePath': '/github-webhook', 'httpMethod': 'POST', 'extendedRequestId': 'cUvx5EM-DoEFSfg=', 'requestTime': '17/Mar/2021:09:05:54 +0000', 'path': '/latest/github-webhook', 'accountId': '189549315145', 'protocol': 'HTTP/1.1', 'stage': 'latest', 'domainPrefix': 'cuicdh0967', 'requestTimeEpoch': 1615971954449, 'requestId': 'c7f48ca9-314e-4b7c-843d-c67354c9af50', 'identity': {'cognitoIdentityPoolId': None, 'accountId': None, 'cognitoIdentityId': None, 'caller': None, 'sourceIp': '', 'principalOrgId': None, 'accessKey': None, 'cognitoAuthenticationType': None, 'cognitoAuthenticationProvider': None, 'userArn': None, 'userAgent': 'GitHub-Hookshot/0cec5b5', 'user': None}, 'domainName': 'cuicdh0967.execute-api.eu-west-1.amazonaws.com', 'apiId': 'cuicdh0967'}, 'body': '{"action":"opened","number":1,"pull_request":{"url":"https://api.github.com/repos/UserName/test-project/pulls/1","id":594532105,"node_id":"MDExOlB1bGxSZXF1ZXN0NTk0NTMyMTA1","html_url":"https://github.com/UserName/test-project/pull/1","diff_url":"https://github.com/UserName/test-project/pull/1.diff","patch_url":"https://github.com/UserName/test-project/pull/1.patch","issue_url":"https://api.github.com/repos/UserName/test-project/issues/1","number":1,"state":"open","locked":false,"title":"add build spec","user":{"login":"userlogin","id":68231264,"node_id":"MDQ6VXNlcjY4MjMxMjY0","avatar_url":"https://avatars.githubusercontent.com/u/68231264?v=4","gravatar_id":"","url":"https://api.github.com/users/userlogin","html_url":"https://github.com/userlogin","followers_url":"https://api.github.com/users/userlogin/followers","following_url":"https://api.github.com/users/userlogin/following{/other_user}","gists_url":"https://api.github.com/users/userlogin/gists{/gist_id}","starred_url":"https://api.github.com/users/userlogin/starred{/owner}{/repo}","subscriptions_url":"https://api.github.com/users/userlogin/subscriptions","organizations_url":"https://api.github.com/users/userlogin/orgs","repos_url":"https://api.github.com/users/userlogin/repos","events_url":"https://api.github.com/users/userlogin/events{/privacy}","received_events_url":"https://api.github.com/users/userlogin/received_events","type":"User","site_admin":false},"body":"","created_at":"2021-03-17T09:04:49Z","updated_at":"2021-03-17T09:04:49Z","closed_at":null,"merged_at":null,"merge_commit_sha":"8a2ae367539ff529219ed453bb2ef4b05fc4789d","assignee":null,"assignees":[],"requested_reviewers":[],"requested_teams":[],"labels":[],"milestone":null,"draft":false,"commits_url":"https://api.github.com/repos/UserName/test-project/pulls/1/commits","review_comments_url":"https://api.github.com/repos/UserName/test-project/pulls/1/comments","review_comment_url":"https://api.github.com/repos/UserName/test-project/pulls/comments{/number}","comments_url":"https://api.github.com/repos/UserName/test-project/issues/1/comments","statuses_url":"https://api.github.com/repos/UserName/test-project/statuses/2fd248bb949d4d674c6f04d84ed0d5bd039e8488","head":{"label":"userlogin:master","ref":"master","sha":"2fd248bb949d4d674c6f04d84ed0d5bd039e8488","user":{"login":"userlogin","id":68231264,"node_id":"MDQ6VXNlcjY4MjMxMjY0","avatar_url":"https://avatars.githubusercontent.com/u/68231264?v=4","gravatar_id":"","url":"https://api.github.com/users/userlogin","html_url":"https://github.com/userlogin","followers_url":"https://api.github.com/users/userlogin/followers","following_url":"https://api.github.com/users/userlogin/following{/other_user}","gists_url":"https://api.github.com/users/userlogin/gists{/gist_id}","starred_url":"https://api.github.com/users/userlogin/starred{/owner}{/repo}","subscriptions_url":"https://api.github.com/users/userlogin/subscriptions","organizations_url":"https://api.github.com/users/userlogin/orgs","repos_url":"https://api.github.com/users/userlogin/repos","events_url":"https://api.github.com/users/userlogin/events{/privacy}","received_events_url":"https://api.github.com/users/userlogin/received_events","type":"User","site_admin":false},"repo":{"id":348632938,"node_id":"MDEwOlJlcG9zaXRvcnkzNDg2MzI5Mzg=","name":"test-project","full_name":"userlogin/test-project","private":true,"owner":{"login":"userlogin","id":68231264,"node_id":"MDQ6VXNlcjY4MjMxMjY0","avatar_url":"https://avatars.githubusercontent.com/u/68231264?v=4","gravatar_id":"","url":"https://api.github.com/users/userlogin","html_url":"https://github.com/userlogin","followers_url":"https://api.github.com/users/userlogin/followers","following_url":"https://api.github.com/users/userlogin/following{/other_user}","gists_url":"https://api.github.com/users/userlogin/gists{/gist_id}","starred_url":"https://api.github.com/users/userlogin/starred{/owner}{/repo}","subscriptions_url":"https://api.github.com/users/userlogin/subscriptions","organizations_url":"https://api.github.com/users/userlogin/orgs","repos_url":"https://api.github.com/users/userlogin/repos","events_url":"https://api.github.com/users/userlogin/events{/privacy}","received_events_url":"https://api.github.com/users/userlogin/received_events","type":"User","site_admin":false},"html_url":"https://github.com/userlogin/test-project","description":"will be trashed after experiments","fork":true,"url":"https://api.github.com/repos/userlogin/test-project","forks_url":"https://api.github.com/repos/userlogin/test-project/forks","keys_url":"https://api.github.com/repos/userlogin/test-project/keys{/key_id}","collaborators_url":"https://api.github.com/repos/userlogin/test-project/collaborators{/collaborator}","teams_url":"https://api.github.com/repos/userlogin/test-project/teams","hooks_url":"https://api.github.com/repos/userlogin/test-project/hooks","issue_events_url":"https://api.github.com/repos/userlogin/test-project/issues/events{/number}","events_url":"https://api.github.com/repos/userlogin/test-project/events","assignees_url":"https://api.github.com/repos/userlogin/test-project/assignees{/user}","branches_url":"https://api.github.com/repos/userlogin/test-project/branches{/branch}","tags_url":"https://api.github.com/repos/userlogin/test-project/tags","blobs_url":"https://api.github.com/repos/userlogin/test-project/git/blobs{/sha}","git_tags_url":"https://api.github.com/repos/userlogin/test-project/git/tags{/sha}","git_refs_url":"https://api.github.com/repos/userlogin/test-project/git/refs{/sha}","trees_url":"https://api.github.com/repos/userlogin/test-project/git/trees{/sha}","statuses_url":"https://api.github.com/repos/userlogin/test-project/statuses/{sha}","languages_url":"https://api.github.com/repos/userlogin/test-project/languages","stargazers_url":"https://api.github.com/repos/userlogin/test-project/stargazers","contributors_url":"https://api.github.com/repos/userlogin/test-project/contributors","subscribers_url":"https://api.github.com/repos/userlogin/test-project/subscribers","subscription_url":"https://api.github.com/repos/userlogin/test-project/subscription","commits_url":"https://api.github.com/repos/userlogin/test-project/commits{/sha}","git_commits_url":"https://api.github.com/repos/userlogin/test-project/git/commits{/sha}","comments_url":"https://api.github.com/repos/userlogin/test-project/comments{/number}","issue_comment_url":"https://api.github.com/repos/userlogin/test-project/issues/comments{/number}","contents_url":"https://api.github.com/repos/userlogin/test-project/contents/{+path}","compare_url":"https://api.github.com/repos/userlogin/test-project/compare/{base}...{head}","merges_url":"https://api.github.com/repos/userlogin/test-project/merges","archive_url":"https://api.github.com/repos/userlogin/test-project/{archive_format}{/ref}","downloads_url":"https://api.github.com/repos/userlogin/test-project/downloads","issues_url":"https://api.github.com/repos/userlogin/test-project/issues{/number}","pulls_url":"https://api.github.com/repos/userlogin/test-project/pulls{/number}","milestones_url":"https://api.github.com/repos/userlogin/test-project/milestones{/number}","notifications_url":"https://api.github.com/repos/userlogin/test-project/notifications{?since,all,participating}","labels_url":"https://api.github.com/repos/userlogin/test-project/labels{/name}","releases_url":"https://api.github.com/repos/userlogin/test-project/releases{/id}","deployments_url":"https://api.github.com/repos/userlogin/test-project/deployments","created_at":"2021-03-17T08:26:50Z","updated_at":"2021-03-17T08:41:21Z","pushed_at":"2021-03-17T08:41:19Z","git_url":"git://github.com/userlogin/test-project.git","ssh_url":"git@github.com:userlogin/test-project.git","clone_url":"https://github.com/userlogin/test-project.git","svn_url":"https://github.com/userlogin/test-project","homepage":null,"size":0,"stargazers_count":0,"watchers_count":0,"language":null,"has_issues":false,"has_projects":true,"has_downloads":true,"has_wiki":true,"has_pages":false,"forks_count":0,"mirror_url":null,"archived":false,"disabled":false,"open_issues_count":0,"license":null,"forks":0,"open_issues":0,"watchers":0,"default_branch":"master","allow_squash_merge":true,"allow_merge_commit":true,"allow_rebase_merge":true,"delete_branch_on_merge":false}},"base":{"label":"UserName:master","ref":"master","sha":"54c9829bb1495223116f4be32fc2bc63425ead83","user":{"login":"UserName","id":29927048,"node_id":"MDEyOk9yZ2FuaXphdGlvbjI5OTI3MDQ4","avatar_url":"https://avatars.githubusercontent.com/u/29927048?v=4","gravatar_id":"","url":"https://api.github.com/users/UserName","html_url":"https://github.com/UserName","followers_url":"https://api.github.com/users/UserName/followers","following_url":"https://api.github.com/users/UserName/following{/other_user}","gists_url":"https://api.github.com/users/UserName/gists{/gist_id}","starred_url":"https://api.github.com/users/UserName/starred{/owner}{/repo}","subscriptions_url":"https://api.github.com/users/UserName/subscriptions","organizations_url":"https://api.github.com/users/UserName/orgs","repos_url":"https://api.github.com/users/UserName/repos","events_url":"https://api.github.com/users/UserName/events{/privacy}","received_events_url":"https://api.github.com/users/UserName/received_events","type":"Organization","site_admin":false},"repo":{"id":348598205,"node_id":"MDEwOlJlcG9zaXRvcnkzNDg1OTgyMDU=","name":"test-project","full_name":"UserName/test-project","private":true,"owner":{"login":"UserName","id":29927048,"node_id":"MDEyOk9yZ2FuaXphdGlvbjI5OTI3MDQ4","avatar_url":"https://avatars.githubusercontent.com/u/29927048?v=4","gravatar_id":"","url":"https://api.github.com/users/UserName","html_url":"https://github.com/UserName","followers_url":"https://api.github.com/users/UserName/followers","following_url":"https://api.github.com/users/UserName/following{/other_user}","gists_url":"https://api.github.com/users/UserName/gists{/gist_id}","starred_url":"https://api.github.com/users/UserName/starred{/owner}{/repo}","subscriptions_url":"https://api.github.com/users/UserName/subscriptions","organizations_url":"https://api.github.com/users/UserName/orgs","repos_url":"https://api.github.com/users/UserName/repos","events_url":"https://api.github.com/users/UserName/events{/privacy}","received_events_url":"https://api.github.com/users/UserName/received_events","type":"Organization","site_admin":false},"html_url":"https://github.com/UserName/test-project","description":"will be trashed after experiments","fork":false,"url":"https://api.github.com/repos/UserName/test-project","forks_url":"https://api.github.com/repos/UserName/test-project/forks","keys_url":"https://api.github.com/repos/UserName/test-project/keys{/key_id}","collaborators_url":"https://api.github.com/repos/UserName/test-project/collaborators{/collaborator}","teams_url":"https://api.github.com/repos/UserName/test-project/teams","hooks_url":"https://api.github.com/repos/UserName/test-project/hooks","issue_events_url":"https://api.github.com/repos/UserName/test-project/issues/events{/number}","events_url":"https://api.github.com/repos/UserName/test-project/events","assignees_url":"https://api.github.com/repos/UserName/test-project/assignees{/user}","branches_url":"https://api.github.com/repos/UserName/test-project/branches{/branch}","tags_url":"https://api.github.com/repos/UserName/test-project/tags","blobs_url":"https://api.github.com/repos/UserName/test-project/git/blobs{/sha}","git_tags_url":"https://api.github.com/repos/UserName/test-project/git/tags{/sha}","git_refs_url":"https://api.github.com/repos/UserName/test-project/git/refs{/sha}","trees_url":"https://api.github.com/repos/UserName/test-project/git/trees{/sha}","statuses_url":"https://api.github.com/repos/UserName/test-project/statuses/{sha}","languages_url":"https://api.github.com/repos/UserName/test-project/languages","stargazers_url":"https://api.github.com/repos/UserName/test-project/stargazers","contributors_url":"https://api.github.com/repos/UserName/test-project/contributors","subscribers_url":"https://api.github.com/repos/UserName/test-project/subscribers","subscription_url":"https://api.github.com/repos/UserName/test-project/subscription","commits_url":"https://api.github.com/repos/UserName/test-project/commits{/sha}","git_commits_url":"https://api.github.com/repos/UserName/test-project/git/commits{/sha}","comments_url":"https://api.github.com/repos/UserName/test-project/comments{/number}","issue_comment_url":"https://api.github.com/repos/UserName/test-project/issues/comments{/number}","contents_url":"https://api.github.com/repos/UserName/test-project/contents/{+path}","compare_url":"https://api.github.com/repos/UserName/test-project/compare/{base}...{head}","merges_url":"https://api.github.com/repos/UserName/test-project/merges","archive_url":"https://api.github.com/repos/UserName/test-project/{archive_format}{/ref}","downloads_url":"https://api.github.com/repos/UserName/test-project/downloads","issues_url":"https://api.github.com/repos/UserName/test-project/issues{/number}","pulls_url":"https://api.github.com/repos/UserName/test-project/pulls{/number}","milestones_url":"https://api.github.com/repos/UserName/test-project/milestones{/number}","notifications_url":"https://api.github.com/repos/UserName/test-project/notifications{?since,all,participating}","labels_url":"https://api.github.com/repos/UserName/test-project/labels{/name}","releases_url":"https://api.github.com/repos/UserName/test-project/releases{/id}","deployments_url":"https://api.github.com/repos/UserName/test-project/deployments","created_at":"2021-03-17T06:06:32Z","updated_at":"2021-03-17T06:06:35Z","pushed_at":"2021-03-17T09:04:50Z","git_url":"git://github.com/UserName/test-project.git","ssh_url":"git@github.com:UserName/test-project.git","clone_url":"https://github.com/UserName/test-project.git","svn_url":"https://github.com/UserName/test-project","homepage":null,"size":0,"stargazers_count":0,"watchers_count":0,"language":null,"has_issues":true,"has_projects":true,"has_downloads":true,"has_wiki":true,"has_pages":false,"forks_count":1,"mirror_url":null,"archived":false,"disabled":false,"open_issues_count":1,"license":null,"forks":1,"open_issues":1,"watchers":0,"default_branch":"master","allow_squash_merge":true,"allow_merge_commit":true,"allow_rebase_merge":true,"delete_branch_on_merge":false}},"_links":{"self":{"href":"https://api.github.com/repos/UserName/test-project/pulls/1"},"html":{"href":"https://github.com/UserName/test-project/pull/1"},"issue":{"href":"https://api.github.com/repos/UserName/test-project/issues/1"},"comments":{"href":"https://api.github.com/repos/UserName/test-project/issues/1/comments"},"review_comments":{"href":"https://api.github.com/repos/UserName/test-project/pulls/1/comments"},"review_comment":{"href":"https://api.github.com/repos/UserName/test-project/pulls/comments{/number}"},"commits":{"href":"https://api.github.com/repos/UserName/test-project/pulls/1/commits"},"statuses":{"href":"https://api.github.com/repos/UserName/test-project/statuses/2fd248bb949d4d674c6f04d84ed0d5bd039e8488"}},"author_association":"CONTRIBUTOR","auto_merge":null,"active_lock_reason":null,"merged":false,"mergeable":true,"rebaseable":true,"mergeable_state":"clean","merged_by":null,"comments":0,"review_comments":0,"maintainer_can_modify":true,"commits":2,"additions":12,"deletions":0,"changed_files":2},"repository":{"id":348598205,"node_id":"MDEwOlJlcG9zaXRvcnkzNDg1OTgyMDU=","name":"test-project","full_name":"UserName/test-project","private":true,"owner":{"login":"UserName","id":29927048,"node_id":"MDEyOk9yZ2FuaXphdGlvbjI5OTI3MDQ4","avatar_url":"https://avatars.githubusercontent.com/u/29927048?v=4","gravatar_id":"","url":"https://api.github.com/users/UserName","html_url":"https://github.com/UserName","followers_url":"https://api.github.com/users/UserName/followers","following_url":"https://api.github.com/users/UserName/following{/other_user}","gists_url":"https://api.github.com/users/UserName/gists{/gist_id}","starred_url":"https://api.github.com/users/UserName/starred{/owner}{/repo}","subscriptions_url":"https://api.github.com/users/UserName/subscriptions","organizations_url":"https://api.github.com/users/UserName/orgs","repos_url":"https://api.github.com/users/UserName/repos","events_url":"https://api.github.com/users/UserName/events{/privacy}","received_events_url":"https://api.github.com/users/UserName/received_events","type":"Organization","site_admin":false},"html_url":"https://github.com/UserName/test-project","description":"will be trashed after experiments","fork":false,"url":"https://api.github.com/repos/UserName/test-project","forks_url":"https://api.github.com/repos/UserName/test-project/forks","keys_url":"https://api.github.com/repos/UserName/test-project/keys{/key_id}","collaborators_url":"https://api.github.com/repos/UserName/test-project/collaborators{/collaborator}","teams_url":"https://api.github.com/repos/UserName/test-project/teams","hooks_url":"https://api.github.com/repos/UserName/test-project/hooks","issue_events_url":"https://api.github.com/repos/UserName/test-project/issues/events{/number}","events_url":"https://api.github.com/repos/UserName/test-project/events","assignees_url":"https://api.github.com/repos/UserName/test-project/assignees{/user}","branches_url":"https://api.github.com/repos/UserName/test-project/branches{/branch}","tags_url":"https://api.github.com/repos/UserName/test-project/tags","blobs_url":"https://api.github.com/repos/UserName/test-project/git/blobs{/sha}","git_tags_url":"https://api.github.com/repos/UserName/test-project/git/tags{/sha}","git_refs_url":"https://api.github.com/repos/UserName/test-project/git/refs{/sha}","trees_url":"https://api.github.com/repos/UserName/test-project/git/trees{/sha}","statuses_url":"https://api.github.com/repos/UserName/test-project/statuses/{sha}","languages_url":"https://api.github.com/repos/UserName/test-project/languages","stargazers_url":"https://api.github.com/repos/UserName/test-project/stargazers","contributors_url":"https://api.github.com/repos/UserName/test-project/contributors","subscribers_url":"https://api.github.com/repos/UserName/test-project/subscribers","subscription_url":"https://api.github.com/repos/UserName/test-project/subscription","commits_url":"https://api.github.com/repos/UserName/test-project/commits{/sha}","git_commits_url":"https://api.github.com/repos/UserName/test-project/git/commits{/sha}","comments_url":"https://api.github.com/repos/UserName/test-project/comments{/number}","issue_comment_url":"https://api.github.com/repos/UserName/test-project/issues/comments{/number}","contents_url":"https://api.github.com/repos/UserName/test-project/contents/{+path}","compare_url":"https://api.github.com/repos/UserName/test-project/compare/{base}...{head}","merges_url":"https://api.github.com/repos/UserName/test-project/merges","archive_url":"https://api.github.com/repos/UserName/test-project/{archive_format}{/ref}","downloads_url":"https://api.github.com/repos/UserName/test-project/downloads","issues_url":"https://api.github.com/repos/UserName/test-project/issues{/number}","pulls_url":"https://api.github.com/repos/UserName/test-project/pulls{/number}","milestones_url":"https://api.github.com/repos/UserName/test-project/milestones{/number}","notifications_url":"https://api.github.com/repos/UserName/test-project/notifications{?since,all,participating}","labels_url":"https://api.github.com/repos/UserName/test-project/labels{/name}","releases_url":"https://api.github.com/repos/UserName/test-project/releases{/id}","deployments_url":"https://api.github.com/repos/UserName/test-project/deployments","created_at":"2021-03-17T06:06:32Z","updated_at":"2021-03-17T06:06:35Z","pushed_at":"2021-03-17T09:04:50Z","git_url":"git://github.com/UserName/test-project.git","ssh_url":"git@github.com:UserName/test-project.git","clone_url":"https://github.com/UserName/test-project.git","svn_url":"https://github.com/UserName/test-project","homepage":null,"size":0,"stargazers_count":0,"watchers_count":0,"language":null,"has_issues":true,"has_projects":true,"has_downloads":true,"has_wiki":true,"has_pages":false,"forks_count":1,"mirror_url":null,"archived":false,"disabled":false,"open_issues_count":1,"license":null,"forks":1,"open_issues":1,"watchers":0,"default_branch":"master"},"organization":{"login":"UserName","id":29927048,"node_id":"MDEyOk9yZ2FuaXphdGlvbjI5OTI3MDQ4","url":"https://api.github.com/orgs/UserName","repos_url":"https://api.github.com/orgs/UserName/repos","events_url":"https://api.github.com/orgs/UserName/events","hooks_url":"https://api.github.com/orgs/UserName/hooks","issues_url":"https://api.github.com/orgs/UserName/issues","members_url":"https://api.github.com/orgs/UserName/members{/member}","public_members_url":"https://api.github.com/orgs/UserName/public_members{/member}","avatar_url":"https://avatars.githubusercontent.com/u/29927048?v=4","description":""},"sender":{"login":"userlogin","id":68231264,"node_id":"MDQ6VXNlcjY4MjMxMjY0","avatar_url":"https://avatars.githubusercontent.com/u/68231264?v=4","gravatar_id":"","url":"https://api.github.com/users/userlogin","html_url":"https://github.com/userlogin","followers_url":"https://api.github.com/users/userlogin/followers","following_url":"https://api.github.com/users/userlogin/following{/other_user}","gists_url":"https://api.github.com/users/userlogin/gists{/gist_id}","starred_url":"https://api.github.com/users/userlogin/starred{/owner}{/repo}","subscriptions_url":"https://api.github.com/users/userlogin/subscriptions","organizations_url":"https://api.github.com/users/userlogin/orgs","repos_url":"https://api.github.com/users/userlogin/repos","events_url":"https://api.github.com/users/userlogin/events{/privacy}","received_events_url":"https://api.github.com/users/userlogin/received_events","type":"User","site_admin":false}}', 'isBase64Encoded': False}