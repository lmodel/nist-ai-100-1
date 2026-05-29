package None;

/* metamodel_version: 1.11.0 */
/* version: 1.0.0 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  A single AI RMF Playbook entry - an enrichment of a Core
subcategory with prose discussion, suggested actions,
documentation questions, references, and topic tags.

Attribute names use the same identifiers found in the published
NIST AI RMF Playbook JSON (e.g., `section_about`,
`section_actions`) so that the data can be loaded directly.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class PlaybookEntry  {

  private String type;
  private String title;
  private String category;
  private String description;
  private String sectionAbout;
  private String sectionActions;
  private String sectionDoc;
  private String sectionRef;
  private List<String> aiActors;
  private List<String> topic;


}