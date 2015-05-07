require 'test_helper'

class ArticleTest < ActiveSupport::TestCase
  test "the truth" do
    Article.create(title: "Hello", text: "Hello world")

    assert Article.count > 0
  end
end
